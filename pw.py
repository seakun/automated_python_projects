#! python3
# pw.py - An insecure password locker program.

PASSWORDS = { 'email': '6Me1^fLuF!FvBI$C@5!CowhAO!@3N',
              'blog': 'jJCaAo7seIWfpjfWC^35*8%q!A4lO',
              'luggage': '1234567890'}

import sys
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSOWRDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)
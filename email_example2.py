import imapclient
# third-party client

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('username', 'password')
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE 20-Aug-2019'])
UIDs
rawMessage = conn.fetch([47474], ['BODY[]', 'FLAGS'])

import pyzmail
# third-party client

message = pyzmail.PyzMessage.factory(rawMesage[47474][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')

message.text_part == None

message.html_part == None

message.text_art_.get_paylod().decode('UTF-8')
message.text_part.charset

conn.list_folders()

conn.select_folder('INBOX', readonly=False)

UIDs = conn.search(['ON 06-Oct-2019'])
UIDs
conn.delete_messages([UIDs])

conn.logout()


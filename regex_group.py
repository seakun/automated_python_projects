import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group())

print('=====================================')

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))

print('=====================================')

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is (415) 555-4242')
print(mo.group())

print('=====================================')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

print('=====================================')

mo = batRegex.search('Batmotorcycle lost a wheel')
print(mo == None)
# print(mo.group())
# AttributeError: 'NoneType'

print('=====================================')

mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(1)) # printing the suffix that's found

import re

# ? - zero or one
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo == None)

print('=================================')

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo == None)

print('=================================')

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo.group())

print('=================================')

# * - zero or more
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo.group())

print('=================================')

# + - one or more
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman')
print(mo == None)
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo.group())

print('=================================')

regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? syntax')
print(mo.group())

print('=================================')

regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? syntax')
print(mo.group())

print('=================================')

regex = re.compile(r'(\+\*\?)+')
mo = regex.search('I learned about +*?+*?+*? syntax')
print(mo.group())


print('=================================')

# {x} - exactly x

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())


phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d\-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo.group())

print('=================================')

# {x, y} - at least x, at most y

haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

haRegex = re.compile(r'(Ha){3,}')
mo = haRegex.search('He said "HaHaHaHaHaHaHaHaHaHaHaHa"')
print(mo.group())

print('=================================')

digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')
print(mo.group()) # matched longest possible string, default syntax

digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group()) # matched smallest possible string




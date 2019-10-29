import re

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
mo = phoneRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo) #findAll() uses lists

# Character classes
# \d, \D
# \w, \W
# \s, \S

print('============================================')

lyrics = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'

xmasRegex = re.compile('\d+\s\w+')
mo = xmasRegex.findall(lyrics)
print(mo)

print('============================================')

vowelRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u)'
mo = vowelRegex.findall('Robocop eats baby food.')
print(mo)

print('============================================')

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}') # r'(a|e|i|o|u)'
mo = doubleVowelRegex.findall('Robocop eats baby food.')
print(mo)

print('============================================')

consonantRegex = re.compile(r'[^aeiouAEIOU]') # everything not a vowel, includes punctuation and numerics
mo = consonantRegex.findall('Robocop eats baby food.')
print(mo)

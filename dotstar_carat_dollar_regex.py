import re

# ^ - begin with this pattern
beginsWithHelloRegex = re.compile(r'^Hello')
mo = beginsWithHelloRegex.search('Hello there!')
print(mo.group())
mo = beginsWithHelloRegex.search('He said "Hello there!"')
print(mo == None)

print('============================================')

# $ - end with this pattern
endsWithWorldRegex = re.compile(r'world!$')
mo = endsWithWorldRegex.search('Hello world!')
print(mo.group())
mo = beginsWithHelloRegex.search('Hello world!adsfasdfasdgasdfa"')
print(mo == None)

print('============================================')

allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('123456789456489156132684')
print(mo.group())
mo = allDigitsRegex.search('123456789456x489156132684')
print(mo == None) # because it has a non-digit character

print('============================================')

# . - anything except newline

atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

print('============================================')

atRegex = re.compile(r'.{1,2}at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

print('============================================')

# .*  - to match anything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.findall('First Name: Al Last Name: Sweigart')
print(mo)

print('============================================')

# (.*) is greedy
# (.*?) is non-greedy

serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
mo = nongreedy.findall(serve)
print(mo)

nongreedy = re.compile(r'<(.*)>')
mo = nongreedy.findall(serve)
print(mo)

print('============================================')

prime = 'Serve the public trust. \nProtect the innocent. \nUphold the law.'
#print(prime)

dotStar = re.compile(r'.*')
mo = dotStar.search(prime)
print(mo.group())

print('============================================')

dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.search(prime)
print(mo.group())

print('============================================')

vowelRegex = re.compile(r'[aeiou]')
mo = vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
print(mo)

print('============================================')

vowelRegex = re.compile(r'[aeiou]', re.I)
mo = vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
print(mo)




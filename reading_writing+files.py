helloFile = open('C:\\Users\\skung.QUANTUMMANAGEME\\Documents\\hello.txt')
content = helloFile.read()

print(content)

helloFile.close()

print("=================================")

helloFile = open('C:\\Users\\skung.QUANTUMMANAGEME\\Documents\\hello.txt')

content = helloFile.readlines()

print(content)

helloFile.close()

print("=================================")

helloFile = open('C:\\Users\\skung.QUANTUMMANAGEME\\Documents\\hello.txt', 'w')

content = helloFile.write('HHHELLLLLLLOOOOO!!!!!\n')
content = helloFile.write('HHHELLLLLLLOOOOO!!!!!\n')
content = helloFile.write('HHHELLLLLLLOOOOO!!!!!\n')
content = helloFile.write('HHHELLLLLLLOOOOO!!!!!\n')
content = helloFile.write('HHHELLLLLLLOOOOO!!!!!\n')

print(content)

helloFile.close()


print("=================================")

helloFile = open('C:\\Users\\skung.QUANTUMMANAGEME\\Documents\\hello.txt', 'a')

content = helloFile.write('append!!!!!\n')
content = helloFile.write('append!!!!!\n')
content = helloFile.write('append!!!!!\n')
content = helloFile.write('append!!!!!\n')

print(content)

helloFile.close()

print("=================================")

import shelve

shelfFile = shelve.open('mydata')
ShelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])


shelfFile = shelve.open('mydata')
shelfFile.keys()
list(shelfFile.keys())
list(shelfFile.values())



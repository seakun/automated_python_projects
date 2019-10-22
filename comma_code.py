def commaCode(listInput):
    newOutput = ''
    for x in listInput:
        if(isinstance(x, int)):
            newOutput += str(x) + ', '
        else:
            newOutput += x + ', '
    return newOutput[:-2]

#spam = ['apples', 'bananas', 'tofu', 'cats']
spam = [1, 2, 3]
print(commaCode(spam))

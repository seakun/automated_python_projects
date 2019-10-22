import pprint

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

pprint.pprint(theBoard)

theBoard['mid-M'] = "X"

pprint.pprint(theBoard)

theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'

theBoard['mid-L'] = 'X'
theBoard['low-R'] = 'X'

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
printBoard(theBoard)

print(type(42))
print(type('hello'))
print(type(3.14))


print(type(theBoard))
print(type(theBoard['top-L']))


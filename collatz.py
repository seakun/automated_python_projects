def collatz(number):
    # if num is even
    if(number % 2 == 0):
        print(number // 2)
        return (number // 2)
    # else num is odd
    else:
        print((3 * number + 1))
        return (3 * number + 1)

print('Enter number: ')
try:
    n = int(input())
except ValueError:
    print('Please input a valid number')
while(n != 1):
    n = collatz(n)

# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class NegativeValueError(Error):
   """Raised when the input value is too small"""
   pass

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) < 0:
        raise NegativeValueError
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a valid number.')
except NegativeValueError:
    print('This is not a valid number.')

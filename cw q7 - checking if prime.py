number = int(input("number: "))

def isPrime(num, test = number-1):
    '''Determines whether an integer value is prime'''
    try:
        if num <= 2 or test == 1:
            return True
        elif num % test != 0:
            return isPrime(num, test-1)
        return False
    except RecursionError:
        return False

print( "%d is a prime number: %s" % (number, isPrime(number)) )

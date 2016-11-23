number1 = int(input("1st number: "))
number2 = int(input("2nd number: "))
List = [4, 19, 23, 36, 40, 43, 61, 64, 78, 95]

def binarySearch(num1, num2, array):
    '''performs binary search to identify if there is
       a number in the List within a given interval'''
    mid = len(array)//2
    try:
        if num1 <= num2:
            if array[mid-1] >= num1 and array[mid-1] <= num2:
                return True
            elif array[mid-1] > num2:
                return binarySearch(num1, num2, array[:mid-1])
            elif array[mid-1] < num1:
                return binarySearch(num1, num2, array[mid:])
            return False
        else:
            return "ERROR! Lower value > upper value"
    except IndexError or RecursionError: ##signifying the two common errors during runtime
        return False

print("Is there an integer between %d and %d in the list? Answer: %s" % (number1, number2, binarySearch(number1, number2, List)))

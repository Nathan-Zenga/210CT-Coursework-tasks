number1 = int(input("1st number: "))
number2 = int(input("2nd number: "))
List = [4, 19, 23, 36, 40, 43, 61, 64, 78, 95]

def binarySearch(num1, num2, array):
    '''performs binary search to identify if there is
       a number in the List within a given interval'''
    mid = len(array)//2
    try:
        if num1 <= num2:                                            ##calls itself with the array halved to the right side of the pivot
            if array[mid-1] >= num1 and array[mid-1] <= num2:
                return True
            elif array[mid-1] > num2:                               ##if the value is larger than pivot (to the right of the array)
                return binarySearch(num1, num2, array[:mid-1])      ##calls itself with the array halved to the right side of the pivot
            elif array[mid-1] < num1:                               ##if the value is smaller than pivot (to the left of the array)
                return binarySearch(num1, num2, array[mid:])        ##calls itself with the array halved to the left side of the pivot
            return False
        else:
            return "ERROR! Lower value > upper value"
    except IndexError or RecursionError:                            ##signifying the two common errors during runtime
        return False

print("Is there an integer between %d and %d in the list? Answer: %s" % (number1, number2, binarySearch(number1, number2, List)))

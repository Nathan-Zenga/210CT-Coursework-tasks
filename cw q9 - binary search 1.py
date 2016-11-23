##num1 = int(input("1st number: "))
##num2 = int(input("2nd number: "))
##li = [4, 19, 23, 36, 40, 43, 61, 64, 78, 95]
##
##def binarySearch(num1, num2):
##    for i in range(len(li)):
##        if li[i] > num1 and li[i] < num2:
##            return True
##    return False
##
##print("%s \t %s" % (li, binarySearch(num1, num2)))


number = int(input("number: "))
list = [4, 19, 23, 36, 40, 43, 61, 64, 78, 95]

def binarySearch(num, array):
    '''performs binary search to identify if there is
       a number in the list within a given interval'''
    mid = len(array)//2
    try:
        if array[mid-1] == num:
            return True
        else:
            if array[mid-1] > num:
                return binarySearch(num, array[:mid-1])
            elif array[mid-1] < num:
                return binarySearch(num, array[mid:])
            return False
    except IndexError and RecursionError: ##signifying the two common errors during runtime
        return False

print("is %d in the list? Answer: %s" % (number, binarySearch(number, list)))

##    for i in range(len(array)-1):
##        print (i, array)
##        if number < array[halfway-1]:
##            array = array[:halfway]
##        elif number > array[halfway-1]:
##            array = array[halfway:]
##        elif number == array[halfway-1]:
##            return True
##    return False

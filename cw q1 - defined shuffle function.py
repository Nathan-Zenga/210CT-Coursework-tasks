from random import *
input1 = [5,3,8,6,1,9,2,7]
print(input1)

def shuff(L):
    '''Randomises order of elements in the taken array'''
    for i in range(len(L)):
        iRandom = randint(0,len(L)-1) # random index in the array
        temp = L[i]         # swapping takes place
        L[i] = L[iRandom]
        L[iRandom] = temp
    return L

print(shuff(input1))

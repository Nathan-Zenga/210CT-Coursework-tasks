from math import sqrt
num = int(input("number: "))

def highestSquareNumber(n):
    ''' Returns closest perfect square number '''

    psn = []                        ## generating perfect square numbers
    for i in range(10000):
        if sqrt(i) % 1 == 0:
            psn.append(i)

    for i in range(len(psn)):       ## returns closest perfect square number
        if n <= psn[i]:
            return psn[i]
            
print( highestSquareNumber(num) )

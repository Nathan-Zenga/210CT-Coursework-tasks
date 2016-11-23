from math import sqrt
num = int(input("number: "))

def highestSquareNumber(x):
    ''' Returns closest perfect square number '''

    psn = []                        ## GENERATING PERFECT SQUARE NUMBERS
    for i in range(10000):
        if sqrt(i) % 1 == 0:
            psn.append(i)

    for i in range(len(psn)):       ## RETURNS CLOSEST PERFECT SQUARE NUMBER
        if x <= psn[i]:
            return psn[i]
            
print( highestSquareNumber(num) )

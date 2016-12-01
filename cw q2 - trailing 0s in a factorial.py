num = int(input("num: "))

def trailingZero(t):
    '''Returns number of trailing zeros of answer from a factorial int'''
    def fact(n):
        '''Returns factorial number of argument'''
        if n == 1:
            return n
        else:
            return n * fact(n-1)
    count = 0
    factAns = str(fact(t))[::-1] # factorial number, converted to string and sequentially reversed
    for i in range(len(factAns)): # counts 0s: stops if no more at trailing end
        if factAns[i] != "0":
            break
        else:
            count+=1
    return count

print(trailingZero(num))

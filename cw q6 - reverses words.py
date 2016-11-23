word = "This is awesome"

def wordReverse(w):
    '''Returns the string argument reversed by word'''
    w = w.split(' ')
    reversedWord = []
##    w = w[::-1]
    for i in range(len(w)-1, -1, -1):
        reversedWord.append(w[i])
    reversedWord = ' '.join(reversedWord)
    return reversedWord

print(wordReverse(word))

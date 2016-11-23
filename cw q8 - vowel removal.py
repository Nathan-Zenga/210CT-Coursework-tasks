word = "beautiful"

def removeVowel(wrd):
    wrd = list(wrd)
    for i in range(len(wrd)):
        if wrd[i] == "a" or wrd[i] == "e" or wrd[i] == "i" or wrd[i] == "o" or wrd[i] == "u":
            wrd[i] = ''
    wrd = ''.join(wrd)
    return wrd

print(removeVowel(word))

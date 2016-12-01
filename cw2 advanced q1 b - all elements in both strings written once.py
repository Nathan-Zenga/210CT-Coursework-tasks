string1 = ['p', 'w', 'q', 'r', 'w', 'a', 'y', 'g', 'z', 'v']
string2 = ['e', 'w', 'u', 't', 'x', 'o', 'u', 'a', 'p', 'a']

s3 = string1 + string2


print(s3)

def unionString(s1, s2):
    count = 0
    for x in range(len(s3)):
        for y in range(len(s3)):
            if s3[x] == s3[y]:
                count = 1
                
            if count == 1:
                s3.pop(x)
                count=0
    
    return s3

##def unionString(s1, s2):
##    count = 0
##    for x in range(len(s1)):
##        for y in range(len(s2)):
##            if s1[x] == s2[y]:
##                count += 1
##                if count  1:
##                    s2.pop(x)
##                    count = 0
##    string3 = s1 + s2
##    return string3


print(unionString(string1, string2))

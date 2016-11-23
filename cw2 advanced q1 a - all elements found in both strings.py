list1 = ['p', 'w', 'q', 'r', 'w', 'a', 'y', 'g', 'z', 'v']
list2 = ['e', 'w', 'u', 't', 'x', 'o', 'u', 'a', 'p', 'a']

def intercept(l1, l2):
    list3 = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                list3.append(l1[i])
##            while i <= len(list3)-1 and j <= len(list3)-1:
##                if list3[i] == list3[j]:
##                    list3.pop(i)
    return list3

print(intercept(list1, list2))

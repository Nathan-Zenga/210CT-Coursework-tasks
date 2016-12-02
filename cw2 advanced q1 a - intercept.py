list1 = ['p', 'w', 'q', 'r', 'w', 'a', 'y', 'g', 'z', 'v']
list2 = ['e', 'w', 'u', 't', 'x', 'o', 'u', 'a', 'p', 'a']

def intercept(l1, l2):
    '''Returns a new list containing all elements present in all given strings'''
    list3 = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:      # checks if element in first string is also found in second string
                list3.append(l1[i]) # appends to list3
    return list3

print(intercept(list1, list2))

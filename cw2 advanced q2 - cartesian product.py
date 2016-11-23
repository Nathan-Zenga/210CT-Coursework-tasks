list1 = ['a', 'b']
list2 = ['x', 'y', 'z']

def cartesian(l1, l2):
    newList = []
    if len(l1) < len(l2):
        for a in range(len(l2)-1):
            for b in range(len(l2)):
                newList.append(l1[a] + l2[b])
    else:
        for a in range(len(l1)-1):
            for b in range(len(l1)):
                newList.append(l2[a] + l1[b])
    return newList

print(cartesian(list1, list2))

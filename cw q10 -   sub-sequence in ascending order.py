n_list = [71, 41, 15, 68, 49, 9, 26, 46, 15, 53, 96]

print(n_list)

##def subSeq(list1):
##    list2 = []
##    lowest = list1[0]
##    for x in range(len(list1)-1):
##        if list1[x+1] > list1[x]:
##            list2.append(list1[x+1])
##    return list2

def subSeq(list1):
    list2 = []
    lowest = list1[0]
    while list1 < :
        for x in range(len(list1)-1):
            if list1[x] < list1[x+1]:
                lowest = list1[x]
        list2.append(lowest)
    return list2

print(subSeq(n_list))

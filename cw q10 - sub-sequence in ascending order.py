array = [71, 41, 15, 68, 49, 9, 26, 46, 15, 53, 96, 23, 54, 17, 11, 5]

print(array, end="\n\n")

def subSeq(list1):
    
    '''Finds and returns ordered sub-sequence within a given list'''

    newList = []  # new list for ordered sub-sequence
    
    while len(list1) >= 2:
        try:
            lowest = list1[0]       # lowest value is first value in given list by default (temp)
            if lowest > list1[1]:
                lowest = list1[1]   # value in second index of the list is now the lowest
                list1 = list1[1:]   # list sequence now starts from point of new lowest value
            else:
                for i in range(1, len(list1)):
                    if lowest > list1[i]:       # checks for smaller integers than lowest value in given list
                        lowest = list1[i]       # value in index i is now the lowest value
                        newList.append(lowest)    # adds new lowest value to new list
                        list1 = list1[i+1:]     # list now starts from index adjacent to that of lowest value
                        for j in range(len(newList[:i])): # code in for-loop deletes every value before last value of new list (lowest) if a smaller value is found
                            if newList[-1] < newList[j]:
                                del newList[:i]
                                break
                        break
                if len(list1) == 2:
                    if newList[-1] < list1[-2] and newList[-1] < list1[-1]:
                        # checks if last value in new list is smaller than last two elements in given list;
                        # if otherwise, following statements are disregards them + returns new list
                        if list1[0] < list1[1]:         # orders remaining values if size length of list is two
                            newList.append(list1[0])
                            newList.append(list1[1])
                        else:
                            newList.append(list1[1])
                        break
        except IndexError:
            break

    return newList

print(subSeq(array))

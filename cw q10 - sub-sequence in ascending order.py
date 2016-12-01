array = [71, 41, 15, 68, 49, 9, 26, 46, 15, 53, 96]
array2 = [71, 41, 15, 68, 49, 9, 26, 46, 15, 53, 96]

print(array, end="\n\n")

def subSeq(list1, list2 = []):
    
    lowest = list1[0]

    if len(list1) == 2:
        list2.append(list1[-1])                 ## last remaining value added to list2 as it is largest by default

    elif lowest > list1[1]:
##        lowest = list1[1]                       ## next index value assigned as lowest vlaue if temp lowest value is bigger than value in the next index
        return subSeq(list1[1:])                ## recall function to read list starting from value in second index (now the temp lowest value)

    elif lowest < list1[1]:
        list2.append(lowest)                    ## append current temp lowest value if next index value smaller than

        if len(list1) == 2:
            list2.append(list1[1])
        else:
            return subSeq(list1, list2)

##        return subSeq(list1[lowest:])         ## recall function to read list starting from lowest value

    return list2

print(subSeq(array))

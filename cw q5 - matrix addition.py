m1 = [[40, 17, 82],
      [13, 30, 93],
      [2, 33, 6]]

m2 = [[35, 89, 22],
      [16, 41, 4],
      [1, 55, 61]]

def addM(matrix1, matrix2):
    '''Returns a new matrix with each value equal to the sum of each index values of the given matrices'''
    newMatrix = [[0 for i in range(len(matrix1[x]))] for x in range(len(matrix1))]
    # 0s added to each index of inner list; inner list added to each index of main list
    # indicates empty spaces to new array, equal to size length of one of given matrices
        
    for i in range(len(matrix1)):
        if len(matrix1) != len(matrix2) or len(matrix1[i]) != len(matrix2[i]): # checks if given matrices are of the same size length for addition to take place
            return None
        else:
            for j in range(len(matrix1[i])):
                newMatrix[i][j] = matrix1[i][j] + matrix2[i][j] # gives sum of vlaues of both given matrices by index
    return newMatrix

print(addM(m1, m2))

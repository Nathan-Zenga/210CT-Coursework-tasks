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
        if len(matrix1) != len(matrix2) or len(matrix1[i]) != len(matrix2[i]):
            return None
        else:
            for j in range(len(matrix1[i])):
                newMatrix[i][j] = matrix1[i][j] + matrix2[i][j] # gives sum of vlaues of both given matrices by index
    return newMatrix

def subM(matrix1, matrix2):
    '''Returns a new matrix with each value equal to the subtraction of each index values of the first matrix by that of the second matrix'''
    newMatrix = [[0 for i in range(len(matrix1[x]))] for x in range(len(matrix1))]
        
    for i in range(len(matrix1)):
        if len(matrix1) != len(matrix2) or len(matrix1[i]) != len(matrix2[i]):
            return None
        else:
            for j in range(len(matrix1[i])):
                newMatrix[i][j] = matrix1[i][j] - matrix2[i][j] # subtracts each value in given matrices
    return newMatrix

def multiM(matrix1, matrix2):
    '''Returns a new matrix with each value equal to the multiplication of given matrices'''
    newMatrix = [[0 for i in range(len(matrix1))] for x in range(len(matrix1[0]))]
    # determines that the dimension product of new matrix will be height (i) of matrix1 and width (j) of matrix2
        
    for i in range(len(matrix1)-1):
        for j in range(len(matrix1[i])-1):
            newMatrix[i][j] = (matrix1[i][j] * matrix2[i][j]) + (matrix1[i][j+1] * matrix2[i+1][j]) # multiplies values in given matrices by index
    return newMatrix

print(addM(m1, m2))
print(subM(m1, m2))

m1 = [[7, 8],
      [0, 9],
      [3, 6]]

m2 = [[5, 9, 2],
      [6, 1, 4]]

print(multiM(m1, m2))

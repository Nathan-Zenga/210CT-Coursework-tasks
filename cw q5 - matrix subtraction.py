m1 = [[40, 17, 82],
      [13, 30, 93],
      [2, 33, 6]]

m2 = [[35, 89, 22],
      [16, 41, 4],
      [1, 55, 61]]

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

print(subM(m1, m2))

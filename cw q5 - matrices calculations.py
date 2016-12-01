m1 = [[40, 17, 82],
      [13, 30, 93],
      [2, 33, 6]]

m2 = [[35, 89, 22],
      [16, 41, 4],
      [1, 55, 61]]

def addM(matrix1, matrix2):
    newMatrix = [[0 for i in range(len(matrix1[x]))] for x in range(len(matrix1))]
    # adding spaces to new array, equal to size length of one of given matrices
        
    for i in range(len(matrix1)):
        if len(matrix1) != len(matrix2) or len(matrix1[i]) != len(matrix2[i]):
            return None
        else:
            for j in range(len(matrix1[i])):
                newMatrix[i][j] = matrix1[i][j] + matrix2[i][j] # adds each value in given matrices by index
                sumElement = newMatrix[i][j]                    
    return newMatrix

print(addM(m1, m2))

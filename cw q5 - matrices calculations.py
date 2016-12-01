m1 = [[87, 14, 77],
      [49, 24, 59],
      [23, 8, 99]]

m2 = [[35, 89, 22],
      [16, 41, 4],
      [1, 55, 61]]

def addM(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        return None
    else:
        newMatrix = [[0 for i in range(len(matrix1[x]))] for x in range(len(matrix1))]
        # adding empty to new array equal to size length of one of given lists
        
        for i in range(len(matrix1)):
            for j in range(len(matrix1[i])):
                newMatrix[i][j] = matrix1[i][j] + matrix2[i][j] # adds each value in given matrices by index
                sumElement = newMatrix[i][j]                    
        return newMatrix

print("%s +\n%s \n= \n%s" % ( m1, m2, addM(m1, m2) ))

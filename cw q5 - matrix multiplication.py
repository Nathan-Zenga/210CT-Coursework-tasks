m1 = [[7, 8],
      [0, 9],
      [3, 6]]

m2 = [[5, 9, 2],
      [6, 1, 4]]

def multiM(matrix1, matrix2):
    '''Returns a new matrix with each value equal to the multiplication of given matrices'''
    newMatrix = [[0 for i in range(len(matrix1))] for x in range(len(matrix1[0]))]
    # determines that the dimension product of new matrix will be height (j) of matrix1 and width (i) of matrix2
        
    for i in range(len(matrix1)-1):
        for j in range(len(matrix1[i])-1):
            newMatrix[i][j] = (matrix1[i][j] * matrix2[i][j]) + (matrix1[i][j+1] * matrix2[i+1][j]) # multiplies values in given matrices by index
    return newMatrix

print(multiM(m1, m2))

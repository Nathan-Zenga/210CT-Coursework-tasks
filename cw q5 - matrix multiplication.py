m1 = [[7, 8],
      [0, 9],
      [3, 6]]

m2 = 2

def multiM(matrix1, matrix2):
    '''Returns a new matrix with each value equal to the multiplication of given matrices'''
    if type(matrix2) == list: # multiplies values in indices from first and second matrix, if second argument is a matrix
        newMatrix = [[0 for i in range(len(matrix1))] for x in range(len(matrix1[0]))]
        # determines that the dimension product of new matrix will be height (i) of matrix1 and width (j) of matrix2

        for i in range(len(matrix1)-1):
            for j in range(len(matrix1[i])-1):
                newMatrix[i][j] = (matrix1[i][j] * matrix2[i][j]) + (matrix1[i][j+1] * matrix2[i+1][j]) # multiplies each index value in given matrix by that of second matrix
    elif type(matrix2) == int: # multiplies values in indices from first matrix by number, if second argument is an integer
        newMatrix = [[0 for i in range(len(matrix1[x]))] for x in range(len(matrix1))]
        number = matrix2 # to identify second argument as number
        for i in range(len(matrix1)):
            for j in range(len(matrix1[i])):
                newMatrix[i][j] = matrix1[i][j] * number
    return newMatrix

print(multiM(m1, m2))

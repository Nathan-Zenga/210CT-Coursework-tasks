m1 = [[7, 8],
      [0, 9],
      [3, 6]]

m2 = [[7, 8],
      [0, 9],
      [3, 6]]

def multiM(matrix1, matrix2):
    '''Returns a new matrix with each value equal to the multiplication of given matrices'''

    newMatrix = [[0 for i in range(len(matrix1[x]))] for x in range(len(matrix1))]
    # determines that the dimension product of new matrix will be height (i) of matrix1 and width (j) of matrix2
    
    if type(matrix2) == list: # multiplies first matrix by second matrix, if second argument is a matrix
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                for k in range(len(matrix2)-1):
                    newMatrix[i][j] += matrix1[i][k] * matrix2[k][j] # multiplies each index value in given matrix by that of second matrix

    elif type(matrix2) == int: # multiplies first matrix by given number, if second argument is an integer
        number = matrix2 # to identify second argument as number
        for i in range(len(matrix1)):
            for j in range(len(matrix1[i])):
                newMatrix[i][j] = matrix1[i][j] * number

    return newMatrix

print(multiM(m1, m2))

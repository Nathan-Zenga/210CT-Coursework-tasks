#    A  B  C  D  E
A = [0, 0, 1, 0, 1]
B = [0, 1, 0, 1, 1]
C = [1, 0, 0, 0, 1]
D = [0, 1, 0, 0, 0]
E = [1, 1, 1, 0, 0]

M = [A, B, C, D, E]

##    M = [[0, 0, 1, 0, 1],
##         [0, 1, 0, 1, 1],
##         [1, 0, 0, 0, 1],
##         [0, 1, 0, 0, 0],
##         [1, 1, 1, 0, 0]]

def isConnected(G):
    '''Determines full-connectedness of the given graph'''

    vertex1 = ord(vertex1)-(ord('A')) # ord(A) = 65 (refers to decimal equivalent of 'A' in ASCII table)
    vertex2 = ord(vertex2)-(ord('A'))
    
    if M[vertex1][vertex2] == 1 and M[vertex2][vertex1] == 1:
        return True
    return False

print(isConnected(M))

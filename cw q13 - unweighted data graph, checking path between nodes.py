class VERTEX

    def __init__(self):
        self.label = 0
        self.edges = []

    def 

example = new VERTEX
example.label = 24
example.edges.append(3)

#    A  B  C  D  E
A = [0, 0, 1, 0, 1]
B = [0, 1, 0, 1, 1]
C = [1, 0, 0, 0, 1]
D = [0, 1, 0, 0, 0]
E = [1, 1, 1, 0, 0]

M = [A, B, C, D, E] # unweighted graph, constructed as an adjacency matrix:
                    #    M = [[0, 0, 1, 0, 1],
                    #         [0, 1, 0, 1, 1],
                    #         [1, 0, 0, 0, 1],
                    #         [0, 1, 0, 0, 0],
                    #         [1, 1, 1, 0, 0]]

def newNode(N, G):
    N = [0 for x in range(len(M))]                          # creates node
    return M.append(N)                                      # adds new node without neighbouring connections    

def addEdge(N, adjacentN, adjacentN2=None, adjacentN3=None):
    for i in range(len(M)):                                 
        for j in range(len(M[i])):
            M[i][j].append(0)
    adjacent = ord(node1) - ord('A')                        # ord(A) = 65 (refers to decimal equivalent of 'A' in ASCII table)
    M[targetNode][adjacent]

#   -----------------------------------

##V = {1,2,3,4}
##E = {{1,4}, {1,2}, {2,3}, {3,4}}
##G = {V, E}

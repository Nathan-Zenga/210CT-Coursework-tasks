B = [[1,2],[4,8]]
C = [[5,7],[6,1]]

sub = __import__('cw q5 - matrix subtraction')
add = __import__('cw q5 - matrix addition')
multi = __import__('cw q5 - matrix multiplication')

r1 = add.addM(B, C)
r2 = multi.multiM(B, C)
r3 = multi.multiM(r1, 2)
## lists returned from above functions are stored

A = sub.subM(r2, r3) ## computes A = B*C - 2*(B+C)

print(r1)
print(r2)
print(r3)
print(A)

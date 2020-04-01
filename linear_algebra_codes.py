# 기본
u = [2,2]
v = [2,3]
z = [3,5]

result = [sum(t) for t in zip(u,v,z)]
print(result)

# vector의 계산 Scalar-Vector product
u = [1,2,3]
v = [4,5,6]
alpha = 2

result = [alpha*sum(t) for t in zip(u,v)]
print(result)

# matrix의 계산 : Matrix addition
matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]
result = [[sum(row)for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result)


# Scalar-Matrix Product
matrix_a = [[3, 6], [4, 5]]
alpha = 4
result = [[ alpha*element for element in t] for t in matrix_a]
print(result)

# Matrix Transpose
#[(1, 4), (2, 5), (3, 6)]
matrix_a = [[1, 2, 3], [4, 5, 6]]
reulst = [[element for element in t] for t in zip(*matrix_a)]
print(reulst)

# Matrix Product
matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[1, 4], [2, 5], [3,6]]
result = [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)
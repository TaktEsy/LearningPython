def get_matrix(n=1, m=1, value=0):
    matrix = []
    for i in range(n, ):
        column = []
        matrix.append(column)
        for c in range(m):
            column.append(value)
    return (matrix)

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
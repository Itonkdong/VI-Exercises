def transform_by_2(matrix):
    new_matrix = [[element * 2 for element in row] for row in matrix]
    return new_matrix


def transform_by_position(matrix):
    new_matrix = [
        [element * 2 for element in matrix[i]] if 0 <= i < len(matrix) / 2 else [element * 3 for element in matrix[i]]
        for i
        in range(len(matrix))]
    return new_matrix


matrix = []

elements = list(map(int, input().split(" ")))
n = elements.pop(0)
m = elements.pop(0)
index = 0

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(elements[index])
        index += 1

print(matrix)
print(transform_by_2(matrix))
print(transform_by_position(matrix))

def rotatematrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[-i - 1][layer]
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]
            matrix[i][- layer - 1] = top

matrix = [[0.0,0.1,0.2],[1.0,1.1,1.2],[2.0,2.1,2.2]]
rotatematrix(matrix)
print(matrix)

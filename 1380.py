matrix = [[7,8],
          [1,2]]
def mat(mats):
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            if matrix[j][i] < matrix[j+1][i]:
                col = matrix[j+1][i]
            else:
                col = matrix[j][i]
            if j + 1 == len(matrix)-1:
                for h in range(len(matrix[i])-1):
                    if matrix[j+1][i] < matrix[j+1][h]:
                        print(matrix[j+1][h])

def matrices(matrix):
    min_row = []
    max_col = []
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        min_row.append(min(matrix[row]))
    for col in range(cols):
        max1 = max(matrix[row][col] for row in range(rows))
        row = row for row in range(rows)
        max_col.append(max1)
    for i in min_row:
        if i in max_col:
            return [i]
#print(matrices(matrix))
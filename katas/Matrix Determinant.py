def get_submatrix(matrix, column):
    return [row[:column] + row[column+1:] for row in matrix[1:]]

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
    sub_determinants = [matrix[0][i] * determinant(get_submatrix(matrix, i)) for i in range(len(matrix))]

    sub_determinants_with_signs = [item if index % 2 == 0 else -1 * item for index, item in enumerate(sub_determinants)]

    return sum(sub_determinants_with_signs)

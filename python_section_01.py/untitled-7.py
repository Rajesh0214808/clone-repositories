def rotate_matrix_90(matrix):
    n = len(matrix)
    # Create an empty matrix for the rotated result
    rotated_matrix = [[0]*n for _ in range(n)]
    
    # Rotate the matrix by 90 degrees clockwise
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n-1-i] = matrix[i][j]
    return rotated_matrix

def transform_matrix(matrix):
    rotated_matrix = rotate_matrix_90(matrix)
    n = len(rotated_matrix)
    
    # Create the final matrix after transformation
    final_matrix = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            # Sum all elements in the same row and column, excluding the current element
            row_sum = sum(rotated_matrix[i]) - rotated_matrix[i][j]
            col_sum = sum(row[j] for row in rotated_matrix) - rotated_matrix[i][j]
            final_matrix[i][j] = row_sum + col_sum
    return final_matrix

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transform_matrix(matrix))

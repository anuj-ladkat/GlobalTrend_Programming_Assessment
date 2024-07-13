def transpose_matrix(matrix):
    """
    Compute the transpose of a 2D list (matrix).
    matrix: 2D list representing the matrix.
    :return: Transposed matrix as a 2D list.
    """
    # Number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Compute transpose using list comprehension
    transpose = [[matrix[row][col] for row in range(rows)] for col in range(cols)]

    return transpose


# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transposed_matrix = transpose_matrix(matrix)
    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("\nTransposed Matrix:")
    for row in transposed_matrix:
        print(row)

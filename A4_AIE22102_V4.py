def transpose_matrix(matrix):
    """
    Calculate the transpose of a matrix.
    """
    return [list(row) for row in zip(*matrix)]

def main():
    """
    Main program to get user input and display results.
    """
    # Get user input for the matrix
    matrix = [list(map(int, input("Enter a row of integers: ").split())) for _ in range(int(input("Enter the number of rows in the matrix: ")))]

    # Calculate the transpose of the matrix
    transpose_result = transpose_matrix(matrix)

    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("\nTranspose of the Matrix:")
    for row in transpose_result:
        print(row)

# Run the main program
main()


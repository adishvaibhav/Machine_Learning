def matrix_multiply(matrix_A, matrix_B):
    """
    Multiply two matrices.
    """
    if len(matrix_A[0]) != len(matrix_B):
        return "Error: Matrices cannot be multiplied."

    result_matrix = [[sum(a * b for a, b in zip(row_A, col_B)) for col_B in zip(*matrix_B)] for row_A in matrix_A]
    return result_matrix

def main():
    """
    Main program to get user input and display results.
    """
    matrix_A = eval(input("Enter matrix A : "))
    matrix_B = eval(input("Enter matrix B : "))

    result = matrix_multiply(matrix_A, matrix_B)

    print("Product of matrices A and B:")
    for row in result:
        print(row)

# Run the main program
main()



def count_common_elements(list1, list2):
    """
    Counts number of common elements between.
    """
    return len(set(list1) & set(list2))

def main():
    """
    Main program to get user input and display results.
    """
    # Get user input for first list
    list1 = [int(x) for x in input("Enter the first list: ").split()]

    # Get user input for second list
    list2 = [int(x) for x in input("Enter the second list: ").split()]

    # Call the function to count common elements
    common_elements_count = count_common_elements(list1, list2)

    # Display results
    print("Number of common elements between the two lists:", common_elements_count)

# Run the main program
main()


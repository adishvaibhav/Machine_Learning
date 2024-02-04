def count_vowels(input_string):
    """
    Function to count the number of vowels in a given input string.
    """
    vowels_set = set("aeiouAEIOU")
    return sum(1 for char in input_string if char.isalpha() and char.lower() in vowels_set)


def count_consonants(input_string):
    """
    Function to count the number of consonants in a given input string.
    """
    vowels_set = set("aeiouAEIOU")
    return sum(1 for char in input_string if char.isalpha() and char.lower() not in vowels_set)


def main():
    """
    Main program to get user input and display results.
    """
    user_input = input("Enter any string: ")  # Receive user input

    num_of_vowels = count_vowels(user_input)
    num_of_consonants = count_consonants(user_input)  # Calls the functions to get counts

    print("Number of vowels:", num_of_vowels)
    print("Number of consonants:", num_of_consonants)  # Display the results


main()  # Run the main program



import pandas as pd

def perform_label_encoding(column):
    """
    Encode a categorical column using label encoding.

    """
    unique_values = set(column)
    encoding = {value: index for index, value in enumerate(unique_values)}
    encoded_column = [encoding[value] for value in column]
    return encoded_column, encoding

def main():
    # Create a synthetic dataset
    data = {'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
            'Value': [10, 20, 15, 25, 30, 22, 18, 27, 24]}

    df = pd.DataFrame(data)

    # Performs label encoding for 'Category'
    encoded_values, encoding_dict = perform_label_encoding(df['Category'])

    # Creates a new DataFrame with encoded values
    df_encoded = pd.DataFrame({'Category_Encoded': encoded_values, 'Value': df['Value']})

    # Display the original and encoded DataFrame
    print("Original DataFrame:")
    print(df)
    print("\nEncoded DataFrame:")
    print(df_encoded)

    # Optional: Inverse transform to get back the original labels
    decoded_labels = [key for key, value in encoding_dict.items()]
    df_encoded['Category_Decoded'] = [decoded_labels[index] for index in df_encoded['Category_Encoded']]
    print("\nDecoded DataFrame:")
    print(df_encoded[['Category_Decoded', 'Value']])

if __name__ == "__main__":
    main()

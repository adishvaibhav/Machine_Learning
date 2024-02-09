import pandas as pd

def perform_one_hot_encoding(df, column_name):
    """
    Perform one-hot encoding for a categorical column in a DataFrame.

    """
    unique_categories = df[column_name].unique()

    # Creates a dictionary for mapping categories to binary vectors
    category_mapping = {category: [1 if cat == category else 0 for cat in unique_categories] for category in unique_categories}

    # Creates a new DataFrame with one-hot encoded values
    df_encoded = pd.DataFrame({f'{column_name}_{category}': df[column_name].map(lambda x: 1 if x == category else 0) for category in unique_categories})
    df_encoded['Value'] = df['Value']

    return df_encoded

def inverse_transform_one_hot(df_encoded):
    """
    Inverse transform one-hot encoded DataFrame to get back the original labels.

    """
    df_decoded = pd.DataFrame({'Category_Decoded': df_encoded.iloc[:, :-1].idxmax(axis=1), 'Value': df_encoded['Value']})
    return df_decoded

def main():
    # Create a synthetic dataset
    data = {'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
            'Value': [10, 20, 15, 25, 30, 22, 18, 27, 24]}

    df = pd.DataFrame(data)

    # Performs one-hot encoding for 'Category'
    df_one_hot = perform_one_hot_encoding(df, 'Category')

    # Displays the original and one-hot encoded DataFrame
    print("Original DataFrame:")
    print(df)
    print("\nOne-Hot Encoded DataFrame:")
    print(df_one_hot)

    # Optional: Inverse transform to get back the original labels
    df_decoded = inverse_transform_one_hot(df_one_hot)
    print("\nDecoded DataFrame:")
    print(df_decoded)

if __name__ == "__main__":
    main()

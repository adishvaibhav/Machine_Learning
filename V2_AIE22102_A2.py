import numpy as np
from collections import Counter

def calculate_euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.
    """
    return np.sqrt(np.sum((point1 - point2)**2))

def k_nearest_neighbors_classifier(training_data, training_labels, new_point, k=3):
    """
    k-Nearest Neighbors classifier.
    """
    distances = [calculate_euclidean_distance(new_point, point) for point in training_data]
    indices = np.argsort(distances)[:k]
    k_nearest_labels = training_labels[indices]

    # Use Counter to find the most common class label among k neighbors
    most_common_label = Counter(k_nearest_labels).most_common(1)[0][0]

    return most_common_label

def main():
    # Example usage:
    # Assume 'training_data' is your feature matrix and 'training_labels' is the corresponding class labels
    training_data = np.array([[1, 2], [2, 3], [3, 1], [4, 5], [5, 4]])
    training_labels = np.array([0, 0, 0, 1, 1])
    new_point = np.array([3.5, 3])

    # Predict the class label for the new_point using k-NN with k=3
    predicted_label = k_nearest_neighbors_classifier(training_data, training_labels, new_point, k=3)
    
if __name__ == "__main__":
    main()



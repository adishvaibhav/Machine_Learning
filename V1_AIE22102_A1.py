import math

def compute_euclidean_distance(point1, point2):
    """
    Compute the Euclidean distance between two points.

    """
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def compute_manhattan_distance(point1, point2):
    """
    Compute the Manhattan distance between two points.

    """
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def main():
    # Example points
    point_a = (3, 4)
    point_b = (5, 8)

    # Calculate distances
    euclidean_result = compute_euclidean_distance(point_a, point_b)
    manhattan_result = compute_manhattan_distance(point_a, point_b)

    # Display results
    print(f"Euclidean Distance: {euclidean_result}")
    print(f"Manhattan Distance: {manhattan_result}")

if __name__ == "__main__":
    main()

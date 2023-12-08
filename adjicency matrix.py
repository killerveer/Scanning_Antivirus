def adjacency_matrix_to_list(matrix):
    adjacency_list = {}
    for i in range(len(matrix)):
        neighbors = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                neighbors.append(j)
        adjacency_list[i] = neighbors
    return adjacency_list

def display_adjacency_list(adjacency_list):
    for vertex, neighbors in adjacency_list.items():
        if neighbors:
            print(f"{vertex} -> {' -> '.join(map(str, neighbors))}")
        else:
            print(f"{vertex} -> (No neighbors)")

# Example adjacency matrix
adjacency_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

# Convert adjacency matrix to adjacency list
adjacency_list = adjacency_matrix_to_list(adjacency_matrix)

# Display the adjacency list
display_adjacency_list(adjacency_list)

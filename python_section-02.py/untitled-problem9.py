import pandas as pd
import numpy as np

def calculate_distance_matrix(file_path):
    # Load the dataset into a DataFrame
    df = pd.read_csv(r"F:\template\python_section-02.py\dataset-2.csv")

    
    # Get the list of unique toll location IDs
    ids = pd.concat([df['id_start'], df['id_end']]).unique()
    
    # Create an empty DataFrame to hold the distance matrix
    distance_matrix = pd.DataFrame(np.inf, index=ids, columns=ids)
    
    # Set the diagonal to 0, as the distance from any point to itself is 0
    np.fill_diagonal(distance_matrix.values, 0)
    
    # Fill in the distances from the dataset
    for _, row in df.iterrows():
        id_start = row['id_start']
        id_end = row['id_end']
        distance = row['distance']
        
        # Set the distances both ways (bidirectional)
        distance_matrix.at[id_start, id_end] = distance
        distance_matrix.at[id_end, id_start] = distance

    # Replace infinities with 0
    distance_matrix.replace(np.inf, 0, inplace=True)

    # Return the final distance matrix
    return distance_matrix

# Specify the correct path to your CSV file
file_path = 'F:/template/dataset-2.csv'

# Call the function to calculate the distance matrix
distance_matrix = calculate_distance_matrix(file_path)

# Print and save the distance matrix
print("Distance Matrix:")
print(distance_matrix)

# Optionally, save the distance matrix to a CSV file
distance_matrix.to_csv('distance_matrix.csv')



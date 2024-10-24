import pandas as pd

# Step 1: Create a CSV file named 'dataset-2.csv'
def create_csv():
    data = {
        'id_start': [1, 1, 2],
        'id_end': [2, 3, 3],
        'distance': [5, 10, 3]
    }
    df = pd.DataFrame(data)
    df.to_csv('dataset-2.csv', index=False)
    print("CSV file 'dataset-2.csv' created successfully!")

# Step 2: Read the CSV file and create the distance matrix
def calculate_distance_matrix():
    distance_df = pd.read_csv('dataset-2.csv')
    
    # Create the distance matrix DataFrame and fill missing values with NaN
    distance_matrix_df = distance_df.pivot(index='id_start', columns='id_end', values='distance')
    
    # Ensure all IDs are represented (1, 2, 3)
    all_ids = [1, 2, 3]
    distance_matrix_df = distance_matrix_df.reindex(all_ids, fill_value=0).reindex(columns=all_ids, fill_value=0)

    # Set diagonal values to 0
    for i in all_ids:
        distance_matrix_df.loc[i, i] = 0
    
    # Print the distance matrix to debug
    print("Distance Matrix before symmetry check:")
    print(distance_matrix_df)

    # Ensure the matrix is symmetric
    for i in all_ids:
        for j in all_ids:
            if i != j:  # Only check if i is not equal to j
                if distance_matrix_df.loc[i, j] == 0:  # If it's 0, copy the distance
                    distance_matrix_df.loc[i, j] = distance_matrix_df.loc[j, i]
    
    print("Distance Matrix after symmetry check:")
    print(distance_matrix_df)
    return distance_matrix_df

# Step 3: Unroll the distance matrix into a DataFrame with three columns
def unroll_distance_matrix(distance_matrix_df):
    unrolled_data = []
    ids = distance_matrix_df.index.tolist()

    for i in ids:
        for j in ids:
            if i != j:  # Exclude the same id_start and id_end
                distance = distance_matrix_df.loc[i, j]
                unrolled_data.append({'id_start': i, 'id_end': j, 'distance': distance})

    # Create a new DataFrame from the unrolled data
    unrolled_df = pd.DataFrame(unrolled_data)
    return unrolled_df

# Main Execution
create_csv()  # Create the CSV file
distance_matrix_df = calculate_distance_matrix()  # Calculate the distance matrix
unrolled_df = unroll_distance_matrix(distance_matrix_df)  # Unroll the distance matrix

print("Unrolled DataFrame:")
print(unrolled_df)







import pandas as pd
import numpy as np

# Step 1: Calculate Distance Matrix (Question 9)
def calculate_distance_matrix():
    # Sample distance data; replace this with your actual CSV data
    data = {
        'id_start': [1, 2, 3],
        'id_end': [2, 3, 1],
        'distance': [5.0, 3.0, 10.0]
    }
    
    distance_df = pd.DataFrame(data)
    # Create a pivot table to create the distance matrix
    distance_matrix_df = distance_df.pivot(index='id_start', columns='id_end', values='distance').fillna(0)
    
    # Ensuring diagonal is 0
    for i in distance_matrix_df.index:
        distance_matrix_df.loc[i, i] = 0
    
    return distance_matrix_df

# Step 2: Unroll Distance Matrix (Question 10)
def unroll_distance_matrix(distance_matrix_df):
    unrolled_data = []
    for i in distance_matrix_df.index:
        for j in distance_matrix_df.columns:
            if i != j:  # Exclude same id_start to id_end
                distance = distance_matrix_df.loc[i, j]
                unrolled_data.append({'id_start': i, 'id_end': j, 'distance': distance})
    
    return pd.DataFrame(unrolled_data)

# Step 3: Calculate Toll Rate (Question 12)
def calculate_toll_rate(distance_df):
    toll_rates = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    
    for vehicle, rate in toll_rates.items():
        distance_df[vehicle] = distance_df['distance'] * rate
    
    return distance_df

# Running the calculations
distance_matrix_df = calculate_distance_matrix()  # Question 9
unrolled_df = unroll_distance_matrix(distance_matrix_df)  # Question 10
toll_rate_df = calculate_toll_rate(unrolled_df)  # Question 12

# Display the final DataFrame with toll rates
print(toll_rate_df)

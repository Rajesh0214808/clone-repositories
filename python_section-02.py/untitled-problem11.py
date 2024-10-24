import pandas as pd

# Sample DataFrame simulating your unrolled distance DataFrame
unrolled_df = pd.DataFrame({
    'id_start': [1, 1, 2, 2, 3, 3, 1, 2],
    'id_end': [2, 3, 1, 3, 1, 2, 4, 4],
    'distance': [5.0, 10.0, 5.0, 3.0, 10.0, 3.0, 7.0, 6.0]  # Added distances for testing
})

# Example reference ID
reference_id = 1

def find_ids_within_ten_percentage_threshold(df, reference_id):
    # Calculate average distance for the reference ID
    distances = df[df['id_start'] == reference_id]['distance']
    average_distance = distances.mean()
    
    # Calculate bounds
    lower_bound = average_distance * 0.9
    upper_bound = average_distance * 1.1
    
    # Find IDs within the threshold
    within_threshold = df[(df['distance'] >= lower_bound) & (df['distance'] <= upper_bound)]
    result_ids = within_threshold['id_end'].unique().tolist()
    
    # Print results
    print(f"Average Distance for ID {reference_id}: {average_distance}")
    print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
    
    return sorted(result_ids)

# Calculate results
result_ids = find_ids_within_ten_percentage_threshold(unrolled_df, reference_id)

# Print final results
print("IDs within 10% threshold:", result_ids)


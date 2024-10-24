import pandas as pd
from datetime import time

# Function from Question 12
def calculate_toll_rate(df):
    toll_rate_df = df.copy()  # Make a copy of the DataFrame
    toll_rate_df['moto'] = toll_rate_df['distance'] * 0.8
    toll_rate_df['car'] = toll_rate_df['distance'] * 1.2
    toll_rate_df['rv'] = toll_rate_df['distance'] * 1.5
    toll_rate_df['bus'] = toll_rate_df['distance'] * 2.2
    toll_rate_df['truck'] = toll_rate_df['distance'] * 3.6
    return toll_rate_df

# Example DataFrame from Question 10
# Ensure to replace this with your actual DataFrame
unrolled_df = pd.DataFrame({
    'id_start': [1, 1, 2, 2, 3, 3],
    'id_end': [2, 3, 1, 3, 1, 2],
    'distance': [5.0, 0.0, 0.0, 3.0, 10.0, 0.0]
})

# Step 1: Calculate toll rates
toll_rate_df = calculate_toll_rate(unrolled_df)

# Function from Question 13
def calculate_time_based_toll_rates(df):
    modified_rows = []
    weekday_factors = {
        'morning': 0.8,  # 00:00 - 10:00
        'day': 1.2,      # 10:00 - 18:00
        'evening': 0.8   # 18:00 - 23:59
    }
    weekend_factor = 0.7
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for _, row in df.iterrows():
        id_start = row['id_start']
        id_end = row['id_end']
        distance = row['distance']

        for day in days_of_week:
            time_intervals = [
                (time(0, 0), time(10, 0), 'morning'),
                (time(10, 0), time(18, 0), 'day'),
                (time(18, 0), time(23, 59), 'evening'),
            ]
            
            for start_time, end_time, period in time_intervals:
                if day in ['Saturday', 'Sunday']:
                    factor = weekend_factor
                else:
                    factor = weekday_factors[period]

                tolls = {
                    'moto': row['moto'] * factor,
                    'car': row['car'] * factor,
                    'rv': row['rv'] * factor,
                    'bus': row['bus'] * factor,
                    'truck': row['truck'] * factor
                }

                modified_rows.append({
                    'id_start': id_start,
                    'id_end': id_end,
                    'start_day': day,
                    'start_time': start_time,
                    'end_day': day,
                    'end_time': end_time,
                    **tolls
                })

    result_df = pd.DataFrame(modified_rows)
    return result_df

# Step 2: Calculate time-based toll rates
time_based_toll_df = calculate_time_based_toll_rates(toll_rate_df)

# Display the resulting DataFrame
print(time_based_toll_df)


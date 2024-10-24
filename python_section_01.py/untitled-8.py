import pandas as pd

# Path to the dataset-1.csv file
file_path = r'F:\template\dataset-1.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Function to check timestamp completeness
def check_timestamp_completeness(df):
    # Ensure the columns are string types
    df['startDay'] = df['startDay'].astype(str).str.strip()
    df['startTime'] = df['startTime'].astype(str).str.strip()
    df['endDay'] = df['endDay'].astype(str).str.strip()
    df['endTime'] = df['endTime'].astype(str).str.strip()

    # Create combined datetime columns
    df['start'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], format='%A %H:%M:%S', errors='coerce')
    df['end'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'], format='%A %H:%M:%S', errors='coerce')

    # Check for any NaT values resulting from bad parsing
    if df['start'].isnull().any() or df['end'].isnull().any():
        print("There were issues parsing some dates.")
        print(df[['start', 'end']][df['start'].isnull() | df['end'].isnull()])

    # Create a multi-index based on 'id' and 'id_2'
    df.set_index(['id', 'id_2'], inplace=True)
    
    # Check for completeness of timestamps
    completeness = {}
    
    # Create time range covering all minutes in a day
    time_range = pd.date_range(start='00:00:00', end='23:59:59', freq='min')

    for (id_start, id_2), group in df.groupby(level=['id', 'id_2']):
        available_times = pd.date_range(start=group['start'].min(), end=group['end'].max(), freq='min')
        
        # Check if all times in the day are covered
        completeness[(id_start, id_2)] = available_times.isin(time_range).all()
    
    return pd.Series(completeness)

# Call the function and print the result
completeness_result = check_timestamp_completeness(df)
print(completeness_result)




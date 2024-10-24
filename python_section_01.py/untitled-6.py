import polyline
import pandas as pd
from math import radians, sin, cos, sqrt, atan2

# Function to decode the polyline and convert to DataFrame
def decode_polyline_to_df(polyline_str):
    # Check if the polyline string is valid
    if not polyline_str:
        raise ValueError("Polyline string is empty or invalid")
    
    # Decode the polyline string into a list of (latitude, longitude) tuples
    try:
        coords = polyline.decode(polyline_str)
    except Exception as e:
        raise ValueError(f"Error decoding polyline string: {e}")
    
    # Create DataFrame with latitude, longitude, and distance (initially 0)
    df = pd.DataFrame(coords, columns=['latitude', 'longitude'])
    df['distance'] = 0.0

    # Calculate distances between successive coordinates
    for i in range(1, len(df)):
        df.loc[i, 'distance'] = haversine(df.loc[i-1, 'latitude'], df.loc[i-1, 'longitude'],
                                          df.loc[i, 'latitude'], df.loc[i, 'longitude'])
    
    return df

# Haversine formula to calculate distance between two latitude-longitude pairs
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Radius of Earth in meters
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)
    a = sin(delta_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Example of a valid polyline string
polyline_str = "_p~iF~ps|U_ulLnnqC_mqNvxq`@"  # Replace this with your polyline string

# Call the function and print the resulting DataFrame
try:
    df = decode_polyline_to_df(polyline_str)
    print(df)
except ValueError as e:
    print(e)

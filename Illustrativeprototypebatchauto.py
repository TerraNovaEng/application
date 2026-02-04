import requests
import csv
import os

"""
RESEARCH ARCHITECTURE NOTE: 
This script illustrates the extraction of live atmospheric telemetry 
into a persistent CSV format for downstream batch verification.
The kbos_to_csv.py script uses the 'a' (append) mode. This means every time you run it, it adds a new row to the bottom of the file without deleting the old ones
"""

def fetch_and_save_to_csv():
    # 1. API Configuration
    headers = {'User-Agent': 'ResearchProject (yourname@email.com)'}
    url = "https://api.weather.gov/stations/KBOS/observations/latest"
    filename = "logan_data.csv"

    try:
        # 2. Extract Data from Website
        response = requests.get(url, headers=headers)
        data = response.json()
        properties = data['properties']
        
        pressure = properties['barometricPressure']['value']
        temp_c = properties['temperature']['value']
        temp_k = temp_c + 273.15  # Conversion to Kelvin

        # 3. Define the Flight Parameters (Fixed for this trial)
        # In a real run, these match your rocket's specs
        row = {
            'cp': 0.35, 
            'cg': 0.28, 
            'p': pressure, 
            't': temp_k, 
            'diam': 0.042
        }

        # 4. Write to CSV
        file_exists = os.path.isfile(filename)
        with open(filename, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            if not file_exists:
                writer.writeheader() # Add headers if it's a new file
            writer.writerow(row)
            
        print(f"Data captured from KBOS: {pressure} Pa at {temp_k} K. Saved to {filename}.")

    except Exception as e:
        print(f"Extraction Error: {e}")

if __name__ == "__main__":
    fetch_and_save_to_csv()
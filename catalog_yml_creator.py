import os
import yaml

# Set the directory where the CSV files are located
data_dir = r"C:\Users\carlf\Documents\GitHub\lyrics_generator\data\01_raw"

# Get a list of all the CSV files in the directory
csv_files = [f for f in os.listdir(data_dir) if f.endswith('_songs')]

# Create a dictionary to store the catalog information
catalog = {}

# Loop through each CSV file and add it to the catalog
for csv_file in csv_files:
    file_path = os.path.join(data_dir, csv_file)
    dataset_name = csv_file.replace('.csv', '')
    catalog[dataset_name] = {
        'source': file_path,
        'description': f'Dataset containing songs information from {dataset_name}'
    }

# Write the catalog information to a YAML file
with open('catalog.yml', 'w') as f:
    yaml.dump(catalog, f, default_flow_style=False)

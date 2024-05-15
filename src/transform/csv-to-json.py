import csv
import json

def convert_csv_to_json(csv_file_path, json_file_path):
    # Initialize the data container
    data = []
    
    # Open the CSV file
    with open(csv_file_path, encoding='utf-8') as csvf:
        # Load CSV content into a dictionary using csv.DictReader
        csv_reader = csv.DictReader(csvf)
        
        # Convert each row into a dictionary and add it to the data
        for row in csv_reader:
            data.append(row)
    
    # Open the JSON file and write the data
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        json.dump(data, jsonf, indent=4)
    
    print("Conversion completed successfully!")

# Example usage:
csv_path = 'input.csv'  # Replace 'input.csv' with the path to your CSV file
json_path = 'old-names.json'  # Desired path for the resulting JSON file

convert_csv_to_json(csv_path, json_path)

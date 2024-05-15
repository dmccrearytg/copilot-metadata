import json

def replace_keys(data, key_map):
    """Recursively replace keys in the nested dictionary."""
    if isinstance(data, dict):
        return {key_map.get(k, k): replace_keys(v, key_map) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_keys(item, key_map) for item in data]
    else:
        return data

def load_json(filename):
    """Load JSON data from a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, filename):
    """Save JSON data to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def main():
    # Load the original data and mappings
    old_data = load_json('old-names.json')
    mappings = load_json('mappings.json')
    
    # Convert the list of mappings into a dictionary
    key_map = {entry['from']: entry['to'] for entry in mappings}
    
    # Replace the keys using the mapping
    new_data = replace_keys(old_data, key_map)
    
    # Save the updated data
    save_json(new_data, 'new-names.json')
    
    print("The JSON keys have been successfully updated.")

if __name__ == "__main__":
    main()

import json

def convert_lists(data):
    """Convert strings in specified fields into arrays of strings."""
    new_data = []
    for item in data:
        # Create a new dictionary for each item
        new_item = {}
        for key, value in item.items():
            # Check if the key ends with 'List' and the value is a string
            if key.endswith('List') and isinstance(value, str):
                # Split the string into an array using newline as the delimiter
                new_item[key] = value.split('\n')
            else:
                # Copy other fields unchanged
                new_item[key] = value
        new_data.append(new_item)
    return new_data

def load_json(filename):
    """Load JSON data from a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, filename):
    """Save JSON data to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def main():
    # Load the original data
    old_data = load_json('new-names.json')
    
    # Convert the required fields
    new_data = convert_lists(old_data)
    
    # Save the updated data
    save_json(new_data, 'list-arrays.json')
    
    print("The data has been successfully updated.")

if __name__ == "__main__":
    main()

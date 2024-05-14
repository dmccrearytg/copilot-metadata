import json
import argparse
from jsonschema import validate, ValidationError, SchemaError

def load_json_file(file_path):
    """Load a JSON file from a given path."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file {file_path}: {e}")
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")

def validate_json(json_data, schema_data):
    """Validate JSON data against the provided schema."""
    try:
        validate(instance=json_data, schema=schema_data)
        print("JSON file is valid against the schema.")
    except ValidationError as ve:
        print(f"JSON validation error: {ve}")
    except SchemaError as se:
        print(f"Schema validation error: {se}")

def main():
    parser = argparse.ArgumentParser(description="Validate JSON against a Schema")
    parser.add_argument("-s", "--schema", type=str, help="Path to JSON schema file", default="schema.json")
    parser.add_argument("-f", "--file", type=str, help="Path to JSON file to validate")
    args = parser.parse_args()

    # Load schema file
    schema_path = args.schema
    try:
        schema_data = load_json_file(schema_path)
    except ValueError as e:
        print(e)
        return

    # Determine the JSON file to validate
    json_path = args.file if args.file else input("Enter the JSON file path to validate: ")

    try:
        json_data = load_json_file(json_path)
        validate_json(json_data, schema_data)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

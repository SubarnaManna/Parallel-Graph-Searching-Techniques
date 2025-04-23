import json 
import os

def read_file(file_path):
    """Reads a JSON file and returns its content as a dictionary."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
        return False
    
    with open(file_path, 'r') as file:
        data = json.load(file)
        file.close()
    return data

def write_file(file_path, data):
    """Writes a dictionary to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        file.close()
    return True
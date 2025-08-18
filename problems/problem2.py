import os

def print_directory_contents(path):
    """Print all files and directories in the given path"""
    print(f"Contents of directory: {path}")
    for item in os.listdir(path):
        print(item)

# Example usage
print_directory_contents('.')  # Current directory
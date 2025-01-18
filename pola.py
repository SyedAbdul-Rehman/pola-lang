#!/usr/bin/env python

import sys
from interpreter import translate_and_execute  # Import your interpreter

def main():
    # Ensure the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: pola file_name.pola")
        return

    # Get the file path from command-line arguments
    file_path = sys.argv[1]

    # Check if the provided file has the .pola extension
    if not file_path.endswith('.pola'):
        print("Error: Please provide a file with the '.pola' extension.")
        return

    try:
        # Run the interpreter on the provided file
        translate_and_execute(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

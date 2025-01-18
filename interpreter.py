# interpreter.py

from keyword_map import keyword_map
from custom_functions import jod,read,write , append_to_file, make_folder# Import the jod function

def translate_and_execute(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()

        # Replace custom keywords with  Python keywords
        # Ensure 'wrna agar' is replaced before 'wrna'
        for custom, python in sorted(keyword_map.items(), key=lambda item: -len(item[0])):
            code = code.replace(custom, python)

        # Define a dictionary for the exec environment
        exec_env = {
        'jod': jod,  # Include jod in the exec environment
        'read': read,  # Include read in the exec environment
        'write': write,
        'append_to_file': append_to_file,
        'make_folder': make_folder# Include write in the exec environment
        }


        # Execute the translated Python code
        exec(code, exec_env)

    except SyntaxError as e:
        print(f"Syntax Error: {e.msg} at line {e.lineno}. Please check your syntax.")
    except NameError as e:
        print(f"Name Error: {e}. It seems like you're using an undefined variable or function.")
    except TypeError as e:
        print(f"Type Error: {e}. Please check the types of the variables or function arguments.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        # Combine the input name and directory to create a relative path to the root folder.
        target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        absolute_working_dir = os.path.abspath(working_directory) # Gets the absolute path for the working_directory parameter.
        valid_working_path = os.path.commonpath([absolute_working_dir, target_file_path]) == absolute_working_dir # Evaluates to a bool comparing the commonpath between the working and target path. True of common path = working directory path
        
        # If the file_path and file type is valid. It will open the file and read it to a string, else return and error.
        if valid_working_path and os.path.isfile(file_path):
            with open(target_file_path, mode='r', errors='replace') as f:
                content_string = f.read(MAX_CHARS)
                if f.read(1):  # If the file exceeded MAX_CHAR limit, prints a message notifying the agent and user that not all of the file was read.
                    content_string += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                    return content_string
                else:
                    return content_string
            return content_string
        
        # Secondary error handling
        elif not os.path.isfile(file_path):
            return ValueError(f'Error: File not found or is not a regular file: "{file_path}"')
        else: 
            return ValueError(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        
    # Initial Error handling
    except ValueError as e:
        print(f'Error: Invalid input directory ({file_path}). Could not retrieve file information.')
    except TypeError as e:
        print(TypeError(f'Error: "{file_path}" is not a directory'))
    except Exception as e: # Catches all unexpected errors to prevent accidental bypass by the LLM.
        print(f'Error: Unexpected error occured: {e}')
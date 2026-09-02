import os

# Giving the agent ability to write and update files based on strict parameters.
def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:

        # Combine the input name and directory to create a relative path to the root folder.
        target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        absolute_working_dir = os.path.abspath(working_directory)
        valid_path = os.path.commonpath([absolute_working_dir, target_file_path]) == absolute_working_dir
        
        if valid_path and not os.path.isfile(file_path):
            os.makedirs(absolute_working_dir, exist_ok=True) # Create any missing directories
            with open(target_file_path, mode='w',) as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written).'
        elif os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory.'
        else:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory.'
        
        # Initial Error handling
    except ValueError as e:
        print(f'Error: Invalid input directory ({file_path}). Could not retrieve file information.')
    except TypeError as e:
        print(TypeError(f'Error: "{working_directory}" is not a directory'))
    except Exception as e: # Catches all unexpected errors to prevent accidental bypass by the LLM.
        print(f'Error: Unexpected error occured: {e}')
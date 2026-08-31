import os
import pathlib

def get_files_info(working_directory: str, directory: str=".") -> str:
    try: # Wrapping in try for validation.
        if isinstance(directory, str):
            work_path_abs = os.path.abspath(working_directory) # Gets the absolute path for the working_directory parameter.
            target_path = os.path.abspath(os.path.join(work_path_abs, directory)) # Resolves the absolute path for the joined 'work_path_abs' var.
            valid_working_path = os.path.commonpath([work_path_abs, target_path]) == work_path_abs # Evaluates to a bool comparing the commonpath between the working and target path. True of common path = working directory path
            if valid_working_path and os.path.isdir(target_path): # Returns error if false to keep the agents grummy hands off that data.
                dir_data = {} # Dictionay key=file_name [value=file_size, file_isdir]
                print(f"Results for {directory} directory:")
                for file in os.listdir(target_path):
                    file_path = os.path.join(target_path, file) # Getting full file_path
                    file_name: str = os.path.basename(file_path) # Getting Filename
                    file_size = os.path.getsize(file_path) # Getting Filesize
                    file_isdir: bool = os.path.isdir(file_path) # Determining if filepath is to another directory
                    dir_data[file_name] = [f"file_size={file_size} bytes", f"is_dir={file_isdir}"] # Adding key/value to dir_data
                    print(f"  - {file_name}: file_size={file_size}, is_dir={file_isdir}") # Printing the results to the console for each file
                return dir_data
            else: # Catches and returns invalid directory requests.
                return print(ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'))
        else:
            return print(TypeError(f'Error: "{directory}" is not a directory'))
    except ValueError as e:
        print(f'Error: Invalid input directory ({directory}). Could not retrieve file information.')
    except TypeError as e:
        print(TypeError(f'Error: "{directory}" is not a directory'))
    except Exception as e: # Catches all unexpected errors to prevent accidental bypass by the LLM.
        print(f'Error: Unexpected error occured: {e}')
        

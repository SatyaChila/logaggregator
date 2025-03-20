import os
 
# Checks if the given folder path exists and returns a list of files in the folder.
def get_files_in_folder(file_path):
    if not os.path.isdir(file_path):
        # Return None if the folder does not exist
        return None  
    # Use os.scandir() for better performance when handling large directories
    return [entry.name for entry in os.scandir(file_path) if entry.is_file()]

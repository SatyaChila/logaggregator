import os

#Checks if the given folder path exists and returns a list of files in the folder.
def get_files_in_folder(file_path):
    if not os.path.isdir(file_path):
        return None  # Return None if the folder does not exist
    return os.listdir(file_path)  # Return list of files in the folder

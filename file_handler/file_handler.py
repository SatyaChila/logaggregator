import os
 
def get_files_in_folder(file_path):
    """
    Checks if the given folder path exists and returns a list of files in the folder.
 
    Parameters:
        file_path (str): The folder path provided by the user.
 
    Returns:
        list: A list of filenames if the folder exists, otherwise None.
    """
    if not os.path.isdir(file_path):
        return None  # Return None if the folder does not exist
 
    return os.listdir(file_path)  # Return list of files in the folder
import os
import sys
 
# Add project root to sys.path for module imports
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
 
# Import necessary modules
from config.constants import *
from file_handler.file_handler import get_files_in_folder
from log_checker.log_checker import count_log_files
 
# Take folder path as input
folder_path = input("Enter the Folder Path: ").strip()
 
# Check if the folder exists
if os.path.isdir(folder_path):
    files = get_files_in_folder(folder_path)  # Get list of files
 
    if files:
        print(PROCESSING_MESSAGE)
 
        # Count log and non-log files
        num_log_files, num_non_log_files = count_log_files(files)
 
        print(f"Log files found: {num_log_files}")
        print(f"Invalid files found: {num_non_log_files}")
 
        if num_log_files == 0:
            print(NO_LOG_FILES_MESSAGE)
    else:
        print(NO_FILES_MESSAGE)
else:
    print(INVALID_PATH)

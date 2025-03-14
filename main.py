import os
import sys

from log_checker.log_checker import *
from log_handler.log_merger import merge_sorted_logs
from file_handler.file_handler import get_files_in_folder
from log_handler import *

#constants
INVALID_PATH = "Invalid Path, Please provide a valid path."
NO_FILES_MESSAGE = "The provided folder has no files in it."
NO_LOG_FILES_MESSAGE = "No log files present in the folder."
PROCESSING_MESSAGE = "Processing...."

# Add project root to sys.path for module imports
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
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
        if num_log_files > 0:
            log_files = [file for file in files if file.endswith(".log")]
            merge_sorted_logs(folder_path, log_files)  # Merge sorted logs
        else:
            print(NO_LOG_FILES_MESSAGE)
    else:
        print(NO_FILES_MESSAGE)
else:
    print(INVALID_PATH)

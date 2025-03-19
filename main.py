import os
import sys
from log_checker.log_checker import count_log_files
from log_handler.log_merger import merge_sorted_logs
from file_handler.file_handler import get_files_in_folder
 
# Constants
FILE_EXTENSION = ".log"
 
# Add project root to sys.path for module imports
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
# Take folder path as input
folder_path = input("Enter the Folder Path: ").strip()
# Check if the folder exists
if os.path.isdir(folder_path):
    # Get list of files
    files = get_files_in_folder(folder_path)  
    if files:
        print("Processing...")
        # Count log and non-log files
        num_log_files, num_non_log_files = count_log_files(files)
        print(f"Log files found: {num_log_files}")
        print(f"Invalid files found: {num_non_log_files}")
        if num_log_files > 0:
            log_files = [file for file in files if file.endswith(FILE_EXTENSION)]
            # Perform merging (but don't save yet)
            merged_logs = merge_sorted_logs(folder_path, log_files)
            # Ask for output folder **after** merging
            output_folder = input("Enter the Output Folder Path: ").strip()
            os.makedirs(output_folder, exist_ok=True)
            # Generate output file name
            output_file = os.path.join(output_folder, merged_logs)
            # Move the file
            os.rename(merged_logs, output_file)  
            print(f"Logs merged and saved to: {output_file}")
        else:
            print("No log files present in the folder.")
    else:
        print("The provided folder has no files in it.")
else:
    print("Invalid Path, Please provide a valid path.")         

import os
from datetime import datetime
from database.db_connection import get_db  # Import the MongoDB connection function
from log_checker.log_checker import count_log_files
from log_handler.log_merger import merge_sorted_logs
from file_handler.file_handler import get_files_in_folder
 
# Constants
FILE_EXTENSION = ".log"
 
# Get MongoDB database and audit collection
db = get_db()
audit_collection = db["audit"]
 
# Take folder path as input
folder_path = input("Enter the Folder Path: ").strip()
operation_time = datetime.now()
 
# Prepare MongoDB audit log entry
audit_entry = {
    "folder_path": folder_path,
    "file_count": 0,
    "log_files": [],
    "operation_time": operation_time,
    "result": "Failed",
    "output_file": None,
    "error_message": None
}
 
# Check if the folder exists
if os.path.isdir(folder_path):
    files = get_files_in_folder(folder_path)
    if files:
        print("Processing...")
        num_log_files, num_non_log_files = count_log_files(files)
        print(f"Log files found: {num_log_files}")
        print(f"Invalid files found: {num_non_log_files}") 
        audit_entry["file_count"] = len(files)
        if num_log_files > 0:
            log_files = [file for file in files if file.endswith(FILE_EXTENSION)]
            audit_entry["log_files"] = log_files
            try:
                # Perform merging (but don't save yet)
                merged_logs = merge_sorted_logs(folder_path, log_files)
                # Ask for output folder after merging
                output_folder = input("Enter the Output Folder Path: ").strip()
                os.makedirs(output_folder, exist_ok=True)
                # Generate output file name
                output_file = os.path.join(output_folder, merged_logs)
                os.rename(merged_logs, output_file)
                print(f"Logs merged and saved to: {output_file}")
                # Update MongoDB audit entry
                audit_entry["result"] = "Success"
                audit_entry["output_file"] = output_file
            except Exception as exception:
                audit_entry["error_message"] = str(exception)
                print(f"Error: {exception}")
        else:
            print("No log files present in the folder.")
            audit_entry["error_message"] = "No log files found."
    else:
        print("The provided folder has no files in it.")
        audit_entry["error_message"] = "No files present in the folder."
else:
    print("Invalid Path, Please provide a valid path.")
    audit_entry["error_message"] = "Invalid folder path."
 
# Insert audit entry into MongoDB
audit_collection.insert_one(audit_entry)
print("Audit entry saved to MongoDB.")

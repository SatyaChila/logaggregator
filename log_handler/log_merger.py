import os
from datetime import datetime
from .log_reader import read_log_file  # Import function to read log files
from .log_handler import extract_timestamp  # Import function to extract timestamps
 
# Define the output file path (use raw string or double backslashes for Windows paths)
OUTPUT_FOLDER = r"C:\satyanarayana_chila\Log\Output"

#Merge log files, sort them by timestamp, and append them to the merged log file.
def merge_sorted_logs(folder_path, log_files):
    # Ensure the output folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    current_datetime = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    # Define the output file path in the output folder
    output_file = os.path.join(OUTPUT_FOLDER, f"logAggegator_Merged_file_{current_datetime}.log")
    all_lines = []
    # Read each log file and collect all lines
    for log_file in log_files:
        file_path = os.path.join(folder_path, log_file)
        all_lines.extend(read_log_file(file_path)) 
    # Sort lines based on timestamp
    sorted_lines = sorted(all_lines, key=extract_timestamp)
    # a appends sorted logs to the output file
    with open(output_file, "a", errors="ignore") as out_file: # a is method, used to append
        out_file.writelines(sorted_lines)
    print(f"Logs merged and saved to: {output_file}")

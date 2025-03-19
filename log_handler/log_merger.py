import os
from datetime import datetime
from .log_reader import read_log_file
from .log_handler import extract_timestamp
 
# Merge log files, sort them by timestamp, and return the merged file path
def merge_sorted_logs(folder_path, log_files):
    current_datetime = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    temp_file = f"logAggregator_Merged_{current_datetime}.log"
    all_lines = []
    # Read each log file and collect all lines
    for log_file in log_files:
        file_path = os.path.join(folder_path, log_file)
        all_lines.extend(read_log_file(file_path))
    # Sort lines based on timestamp
    sorted_lines = sorted(all_lines, key=extract_timestamp)
    # a appends sorted logs to the output file
    with open(temp_file, "a", errors="ignore") as out_file:
        out_file.writelines(sorted_lines)
    # Return the file name, not the full path
    return temp_file  

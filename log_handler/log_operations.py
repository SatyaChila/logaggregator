import os
import re
from datetime import datetime
from log_handler.log_reader import read_log_file

def extract_timestamp(log_line):
    # Generalized regex to capture various timestamp formats
    # Matches timestamps in formats like "YYYY/MM/DD HH:MM:SS.sss" or "DD-MM-YYYY HH:MM:SS:sss"
    timestamp_pattern = r"(\d{2,4}[/.-]\d{2}[/.-]\d{2,4} \d{2}:\d{2}:\d{2}[.:]\d+)"
    match = re.search(timestamp_pattern, log_line)
    if match:
        timestamp_str = match.group(1)
        # Possible timestamp formats
        formats = [
            "%m/%d/%Y %H:%M:%S.%f",
            "%Y/%m/%d %H:%M:%S:%f",
            "%Y-%m-%d %H:%M:%S.%f"
        ]
        for fmt in formats:
            try:
                return datetime.strptime(timestamp_str, fmt)
            except ValueError:
                continue
    return datetime.min

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
    # Return a default datetime if no valid timestamp is found
        return temp_file 

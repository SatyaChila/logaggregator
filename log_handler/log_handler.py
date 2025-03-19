import os
from datetime import datetime

#Extract timestamp from a log line, returning datetime.min if parsing fails.
def extract_timestamp(line):
    try:
        timestamp_str = line.split()[0].strip("[]")
        return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    except (IndexError, ValueError):
        # Default to the earliest date
        return datetime.min  

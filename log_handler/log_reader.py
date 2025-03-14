#Read a log file and return its lines.  
def read_log_file(file_path):
    try:
        with open(file_path, "r", errors="ignore") as file:
            return file.readlines()
    except Exception as e:
        print(f"Skipping {file_path} due to error: {e}")
        return []

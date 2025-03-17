#Read a log file and return its lines.  
def read_log_file(file_path):
    try:
        #r opens a file for reading
        with open(file_path, "r", errors="ignore") as file:
            return file.readlines()
    # Exception is stored in exception to know the error in print statement
    except Exception as exception:
        print(f"Skipping {file_path} due to error: {exception}")
        return []

# Counts the number of log files and non-log files in a given list of files.
def count_log_files(files):
    no_of_log_files = 0
    no_of_non_log_files = 0
    for file in files:
        if file.endswith(".log"):  
            # Increment count for .log files
            no_of_log_files += 1  
        else:
            # Increment count for other files
            no_of_non_log_files += 1   
    # Ensure it returns a tuple
    return (no_of_log_files, no_of_non_log_files)  

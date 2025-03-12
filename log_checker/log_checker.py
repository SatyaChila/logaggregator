def count_log_files(files):
    """
    Counts the number of log files and non-log files in a given list of files.
 
    Parameters:
        files (list): A list of filenames from the folder.
 
    Returns:
        tuple: (number of log files, number of non-log files)
    """
    no_of_log_files = 0
    no_of_non_log_files = 0
 
    for file in files:
        if file.endswith(".log"):  
            no_of_log_files += 1  # Increment count for .log files
        else:
            no_of_non_log_files += 1  # Increment count for other files
 
    return no_of_log_files, no_of_non_log_files
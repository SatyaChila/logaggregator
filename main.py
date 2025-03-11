import os # interacts with system files

path=input("Enter the  Folder Path:") #Taking path as an input


if os.path.isdir(path): #Checks the folder is present or not
    files = os.listdir(path) # returns the list of files
    
    if files:
        print("Processing....")

        no_of_log_files=0
        no_of_non_log_files=0

        for file in files:# checks each file in the directory
            if file.endswith(".log"): # checks if the file ends with .log
                no_of_log_files += 1
            else:
                no_of_non_log_files+=1
        if no_of_log_files > 0: #It checks each and every file
            print(f"Log files found:{no_of_log_files}")
            print(f"Invalid file found:{no_of_non_log_files}")
        elif no_of_log_files == 0:#It checks for if it does'nt contain log files
            print(f"Log files found:{no_of_log_files}")
            print(f"Invalid log files:{no_of_non_log_files}")
            print("The provided folder doesn't have log files in it.")   
    else:
        print("The provided folder has no files in it.")
else:
    print("Inavalid Path, Please provide the valid path.")


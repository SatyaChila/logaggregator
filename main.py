import os # interacts with system files

path=input("Enter the  Folder Path:") #Taking path as an input

print("processing....")#The get information that the process is started

if os.path.isdir(path): #Checks the folder is present or not
    files = os.listdir(path) # returns the list of files
    
    if files:
        print("Files exist in the folder")

        no_of_log_files=0
        no_of_non_log_files=0

        for file in files:# checks each file in the directory
            if file.endswith(".log"): # checks if the file ends with .log
                no_of_log_files += 1
            else:
                no_of_non_log_files+=1
        if no_of_log_files>0 and no_of_non_log_files == 0:# checks for only log files
            print(f"Log files found:{no_of_log_files}")
        else:
            print("It has non log files in it please provide files which has non log files.")   
            
    else:
        print("Please provide the path which has files in it.")
else:
    print("Inavalid Path, Please provide the correct path.")


import os # interacts with system files

path=input("Enter the  Folder Path:") #Taking path as an input
if os.path.isdir(path): #Checks the folder is present or not
    files = os.listdir(path) # returns the list of files
    if files:
        print("files exists in the folder")
        for file in files:
            if file.endswith(".log"): # checks if the file ends with .log
                print("log files found")                
            else:
                print("It has different extensions")     
    else:
        print("No files in the folder")
    print("processing")
else:
    print("Inavalid Path")


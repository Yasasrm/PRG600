''' 
Name: Yasas Maddumage. 
Student ID: 170308233. 
Description: Lab 6 part 1 Question 5 (lab8e.py).  
''' 

import os
import shutil
import sys

def getDirectoryPath():
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python lab8e.py <directory_path>")
        sys.exit(1)
    # Get the directory path from command line arguments
    return sys.argv[1]

def isValidDirectory(directoryPath):
    # Check if the provided path is a valid directory
    if not os.path.isdir(directoryPath):
        return False
    return True
        
def getBackupLocation(directoryPath):
    # Get the absolute path of the directory
    absDirectoryPath = os.path.abspath(directoryPath)
    # backups directory
    return os.path.join(absDirectoryPath, 'backups')

def createBackupDirectoryIfNotExist(backupsDir):
    # Create the backups directory if it does not exist
    if not os.path.exists(backupsDir):
        os.makedirs(backupsDir)

def backup(directory, backupsDir):
    # Walk through the directory and process files
    for root, dirs, files in os.walk(os.path.abspath(directory)):
        # Skip the backups directory itself
        if root == backupsDir:
            continue

        for fileName in files:
            # Check if the file is a Python script
            if fileName.endswith('.py'):
                # Define the full path for the source file and destination file
                sourceFile = os.path.join(root, fileName)
                destinationFile = os.path.join(backupsDir, fileName)
                
                # Check if a file with the same name exists in the backups directory
                if os.path.exists(destinationFile):
                    # Append a number to the file name to avoid overwriting
                    base, ext = os.path.splitext(fileName)
                    counter = 1
                    while os.path.exists(destinationFile):
                        newFileName = f"{base}_{counter}{ext}"
                        destinationFile = os.path.join(backupsDir, newFileName)
                        counter += 1

                # Copy the Python script to the backups directory
                shutil.copy(sourceFile, destinationFile)
                print(f"Copied '{sourceFile}' to '{destinationFile}'")

if __name__ == "__main__":
    directory = getDirectoryPath()
    if(isValidDirectory(directory)):
        backupPath = getBackupLocation(directory)
        createBackupDirectoryIfNotExist(backupPath)
        backup(directory, backupPath)
    else:
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)
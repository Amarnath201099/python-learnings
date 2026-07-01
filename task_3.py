# Task 3: Safe File Reader
# Objective: Read files safely with proper error handling.

import os

file_name = input("Enter file name: ")

if not file_name:
    print("Enter valid file name")
    exit()

if not file_name.endswith(".txt"):
    file_name += ".txt"

file_path = os.path.join(os.path.dirname(__file__), file_name)

try:
    with open(file_path, "r") as file:
        data = file.read()
        print(data)

    # Below code reads the file from the current working directory (CWD)
    # with open(file_name, "r") as file:
    #     data = file.read()
    #     print(data)
except FileNotFoundError:
    print("File does't exist by name ", file_name)
finally:
    print("File reading completed")





# 🔹 os module is used to interact with the operating system (Windows, macOS, Linux)
# It helps us handle file paths in a safe and platform-independent way
#
# Why we use os.path.join():
# - Different operating systems use different path separators:
#   Windows → \
#   Linux/Mac → /
# - os.path.join() automatically uses the correct separator for your OS
#
# Why we use os.path.dirname(__file__):
# - __file__ gives the path of the current Python file
# - dirname(__file__) gives the folder where this script is located
# - This ensures we always look for files in the SAME folder as the script
#
# This avoids errors caused by running the script from a different directory (CWD issue)


# 🔹 Important os module basics:
#
# os.getcwd() → shows current working directory (where Python is running)
# os.listdir(path) → lists all files and folders in a directory
# os.path.exists(path) → checks if file/folder exists
# os.path.isfile(path) → checks if path is a file
# os.path.isdir(path) → checks if path is a folder
# os.path.join(a, b) → safely joins folder and file names
# os.path.dirname(path) → returns folder part of a path

# 🔹 What else can we do with "with open()" besides reading:

# 1. Write to a file (overwrite existing content)
# with open("file.txt", "w") as file:
#     file.write("Hello World")

# 2. Append to a file (add content without deleting old data)
# with open("file.txt", "a") as file:
#     file.write("New line added")

# 3. Read line by line (memory efficient for large files)
# with open("file.txt", "r") as file:
#     for line in file:
#         print(line)

# 4. Read all lines into a list
# with open("file.txt", "r") as file:
#     lines = file.readlines()

# 5. Read first N characters
# with open("file.txt", "r") as file:
#     data = file.read(10)

# 🔹 Key idea:
# "with open()" can be used for read (r), write (w), append (a)
# It automatically closes the file after the block ends (safe handling)
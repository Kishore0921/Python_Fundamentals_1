'''
File Handling in Python is a way to work with files on your computer. 
It allows you to read from and write to files, which can be useful for storing data, logging information, or processing text. 
Python provides built-in functions and methods to handle files easily.
File Handling
File Handling is the process of working with files on your computer through a program -
that is, creating, opening, reading, writing, appending, and deleting files using code.

What is File Handling?
File Handling allows a Python program to interact with files stored on disk. It lets a
program save data permanently (unlike variables, which are lost once the program ends).

Why File Handling is Used?
- To store data permanently, even after the program stops running.
- To read data that already exists (like configuration files, logs, or reports).
- To share data between different programs or program runs.
- To keep records such as logs, notes, or student marks without needing a database.

Note: This file intentionally does NOT use try/except/finally or exception handling of any
kind (as requested). Instead, checks like os.path.exists() are used beforehand to keep the
file operations safe, so the script can be run multiple times without errors.
'''

import os

# ------------------------------------------------------------------
# Internal cleanup so this script can be run again and again safely,
# without try/except. This simply removes leftover demo files/folders
# from any previous run.
# ------------------------------------------------------------------
cleanup_files = [
    "sample.txt", "mode_demo.txt", "binary_file.bin",
    "renamed_file.txt", "copy_of_sample.txt",
    "student_marks.txt", "notes.txt", "log.txt"
]
for file_name in cleanup_files:
    if os.path.exists(file_name):
        os.remove(file_name)

if os.path.exists("demo_folder"):
    os.rmdir("demo_folder")


# 1. Creating a New File (x mode)
print("\n======1. Creating a New File (x mode)======")
# 'x' mode creates a new file, and raises an error if the file already exists.
# Since we cleaned up above, this file does not exist yet, so it is safe to create.
new_file = open("sample.txt", "x")
new_file.write("Hello, this is a sample file.\nThis file is used for the file handling demo.\n")
new_file.close()
print("File 'sample.txt' created successfully using 'x' mode")


# 2. Opening a File
print("\n======2. Opening a File======")
# open() is used to open a file. It needs a filename and, optionally, a mode (default is 'r')
opened_file = open("sample.txt", "r")
print("File opened using open():", opened_file)
opened_file.close()


# 3. Reading Files
print("\n======3. Reading Files======")

# read() reads the entire content of the file as a single string
file_for_read = open("sample.txt", "r")
print("Using read():")
print(file_for_read.read())
file_for_read.close()

# readline() reads just ONE line at a time from the file
file_for_readline = open("sample.txt", "r")
print("Using readline() (first call):", file_for_readline.readline().strip())
print("Using readline() (second call):", file_for_readline.readline().strip())
file_for_readline.close()

# readlines() reads all lines and returns them as a list of strings
file_for_readlines = open("sample.txt", "r")
print("Using readlines():", file_for_readlines.readlines())
file_for_readlines.close()


# 4. Writing Files
print("\n======4. Writing Files======")
# 'w' mode opens a file for writing; it OVERWRITES the existing content completely
file_for_write = open("sample.txt", "w")

# write() writes a single string to the file
file_for_write.write("This line replaces the old content using write().\n")

# writelines() writes a list of strings to the file, one after another
file_for_write.writelines(["Second line using writelines().\n", "Third line using writelines().\n"])
file_for_write.close()

file_check_write = open("sample.txt", "r")
print("Content after writing:")
print(file_check_write.read())
file_check_write.close()


# 5. Appending Data (append mode 'a')
print("\n======5. Appending Data======")
# 'a' mode opens a file for writing too, but ADDS new content to the END instead of overwriting
file_for_append = open("sample.txt", "a")
file_for_append.write("This line was added using append mode.\n")
file_for_append.close()

file_check_append = open("sample.txt", "r")
print("Content after appending:")
print(file_check_append.read())
file_check_append.close()


# 6. Closing Files
print("\n======6. Closing Files======")
# close() releases the file so other programs (or parts of your program) can safely use it
file_to_close = open("sample.txt", "r")
print("Is file closed before calling close()?", file_to_close.closed)
file_to_close.close()
print("Is file closed after calling close()?", file_to_close.closed)


# 7. Using the with Statement
print("\n======7. Using the with Statement======")
# with open() automatically closes the file once the indented block finishes running,
# even without explicitly calling close() - this is the recommended way to work with files
with open("sample.txt", "r") as with_file:
    print("Content read using 'with open()':")
    print(with_file.read())

# Automatic File Closing
print("Is file closed automatically after the 'with' block?", with_file.closed)


# 8. File Modes
print("\n======8. File Modes======")
# r  - Read (default): opens a file for reading; the file must already exist
# w  - Write: opens a file for writing; creates the file if missing, overwrites if it exists
# a  - Append: opens a file for writing; creates the file if missing, adds to the end if it exists
# x  - Create: creates a new file; raises an error if the file already exists
# t  - Text Mode (default): reads/writes data as normal text/strings
# b  - Binary Mode: reads/writes data as raw bytes (used for non-text files like images)
# r+ - Read and Write: file must already exist; allows both reading and writing
# w+ - Write and Read: creates/overwrites the file; allows both writing and reading
# a+ - Append and Read: creates the file if missing; allows both appending and reading

print("\nDemonstrating r+, w+, and a+:")

# r+ : file must already exist; supports both reading and writing
file_r_plus = open("sample.txt", "r+")
print("r+ mode - existing content:", file_r_plus.readline().strip())
file_r_plus.write("Line added using r+ mode.\n")
file_r_plus.close()

# w+ : creates/overwrites the file, then allows reading it back
file_w_plus = open("mode_demo.txt", "w+")
file_w_plus.write("Content written using w+ mode.\n")
file_w_plus.seek(0)  # move back to the beginning before reading
print("w+ mode - content read back:", file_w_plus.read().strip())
file_w_plus.close()

# a+ : appends to the file (creating it if needed), then allows reading it back
file_a_plus = open("mode_demo.txt", "a+")
file_a_plus.write("Extra content added using a+ mode.\n")
file_a_plus.seek(0)  # move back to the beginning before reading
print("a+ mode - full content read back:", file_a_plus.read())
file_a_plus.close()


# 9. File Pointer - tell()
print("\n======9. File Pointer - tell()======")
# tell() returns the current position of the file pointer (in bytes) within the file
file_for_tell = open("sample.txt", "r")
print("Pointer position right after opening:", file_for_tell.tell())
file_for_tell.read(10)  # read the first 10 characters
print("Pointer position after reading 10 characters:", file_for_tell.tell())
file_for_tell.close()


# 10. File Pointer - seek()
print("\n======10. File Pointer - seek()======")
# seek() moves the file pointer to a specific position, so the next read/write starts from there
file_for_seek = open("sample.txt", "r")
file_for_seek.read(10)
print("Pointer position before seek():", file_for_seek.tell())
file_for_seek.seek(0)  # move the pointer back to the beginning of the file
print("Pointer position after seek(0):", file_for_seek.tell())
print("Reading again from the start:", file_for_seek.readline().strip())
file_for_seek.close()


# 11. Checking File Properties
print("\n======11. Checking File Properties======")
file_for_properties = open("sample.txt", "r")
# name - shows the name/path of the file that was opened
print("File name:", file_for_properties.name)
# mode - shows the mode the file was opened in
print("File mode:", file_for_properties.mode)
# closed - shows whether the file is currently closed (True) or open (False)
print("Is file closed?", file_for_properties.closed)
file_for_properties.close()
print("Is file closed now?", file_for_properties.closed)


# 12. Reading and Writing Binary Files
print("\n======12. Reading and Writing Binary Files======")
# 'wb' opens a file for writing in binary mode (data must be given as bytes, not normal strings)
binary_write_file = open("binary_file.bin", "wb")
binary_write_file.write(b"Binary data example")
binary_write_file.close()
print("Binary file 'binary_file.bin' written using 'wb' mode")

# 'rb' opens a file for reading in binary mode (returns bytes, not a normal string)
binary_read_file = open("binary_file.bin", "rb")
print("Content read using 'rb' mode:", binary_read_file.read())
binary_read_file.close()


# 13. Renaming Files - os.rename()
print("\n======13. Renaming Files======")
# os.rename(old_name, new_name) renames (or moves) a file
os.rename("mode_demo.txt", "renamed_file.txt")
print("'mode_demo.txt' renamed to 'renamed_file.txt'")


# 14. Deleting Files - os.remove()
print("\n======14. Deleting Files======")
# os.remove(file_name) permanently deletes the specified file
temp_file_to_delete = open("temp_delete_me.txt", "w")
temp_file_to_delete.write("This file will be deleted shortly.")
temp_file_to_delete.close()
print("Temporary file 'temp_delete_me.txt' created")
os.remove("temp_delete_me.txt")
print("Temporary file deleted using os.remove()")


# 15. Checking File Existence - os.path.exists()
print("\n======15. Checking File Existence======")
# os.path.exists(path) returns True if the file/folder exists, False otherwise
print("Does 'sample.txt' exist?", os.path.exists("sample.txt"))
print("Does 'temp_delete_me.txt' exist (already deleted)?", os.path.exists("temp_delete_me.txt"))


# 16. Creating Directories - os.mkdir()
print("\n======16. Creating Directories======")
# os.mkdir(folder_name) creates a new, single directory/folder
os.mkdir("demo_folder")
print("Directory 'demo_folder' created using os.mkdir()")
print("Does 'demo_folder' exist now?", os.path.exists("demo_folder"))


# 17. Removing Directories - os.rmdir()
print("\n======17. Removing Directories======")
# os.rmdir(folder_name) removes a directory, but ONLY if it is completely empty
os.rmdir("demo_folder")
print("Directory 'demo_folder' removed using os.rmdir()")
print("Does 'demo_folder' exist now?", os.path.exists("demo_folder"))


# 18. Listing Files - os.listdir()
print("\n======18. Listing Files======")
# os.listdir(path) returns a list of all the files and folders inside the given directory
current_directory_items = os.listdir(".")
print("Items in the current directory:", current_directory_items)


# 19. Copying File Content
print("\n======19. Copying File Content======")
# A file's content can be copied into another file simply by reading from one and writing to
# the other (without needing any extra library)
source_file = open("sample.txt", "r")
destination_file = open("copy_of_sample.txt", "w")
destination_file.write(source_file.read())
source_file.close()
destination_file.close()
print("Content copied from 'sample.txt' to 'copy_of_sample.txt'")

copy_check_file = open("copy_of_sample.txt", "r")
print("Content of the copied file:")
print(copy_check_file.read())
copy_check_file.close()


# Working with Paths
print("\n======Working with Paths======")
# Relative Path - a path given relative to the current working directory (e.g. "sample.txt")
print("Relative Path example:", "sample.txt")

# Absolute Path (Introduction) - the full path starting from the root of the file system
print("Absolute Path (Introduction) of 'sample.txt':", os.path.abspath("sample.txt"))
print("Current Working Directory:", os.getcwd())


# File Handling Example
print("\n======File Handling Example======")

# Student Marks File
print("\nStudent Marks File:")
with open("student_marks.txt", "w") as marks_file:
    marks_file.write("Math: 90\n")
    marks_file.write("Science: 85\n")
    marks_file.write("English: 78\n")

with open("student_marks.txt", "r") as marks_file:
    print("Contents of 'student_marks.txt':")
    print(marks_file.read())

# Notes File
print("Notes File:")
with open("notes.txt", "w") as notes_file:
    notes_file.write("Remember to revise OOP concepts.\n")
    notes_file.write("Practice file handling examples daily.\n")

with open("notes.txt", "r") as notes_file:
    print("Contents of 'notes.txt':")
    print(notes_file.read())

# Simple Log File
print("Simple Log File:")
with open("log.txt", "a") as log_file:
    log_file.write("Program started successfully.\n")
    log_file.write("File handling demo executed.\n")

with open("log.txt", "r") as log_file:
    print("Contents of 'log.txt':")
    print(log_file.read())


# Best Practices
print("\n======Best Practices======")
print("1. Always close files after use, so resources are released properly.")
print("2. Prefer the 'with' statement, since it closes files automatically, even if")
print("   an error occurs while working with the file.")
print("3. Check whether a file exists (os.path.exists()) before trying to delete it,")
print("   to avoid trying to remove a file that is not there.")
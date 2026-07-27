# Write in the py file

f = open("python/example.txt", "w")  # Open a file in write mode
f.write("Hello, World!\n")  # Write a string to the file
f.write("This is an example of file handling in Python.\n")  # Write another string to the file
f.close()  # Close the file

# Cant perform any read or the write operation after closing the file. If you try to do so, it will raise a ValueError.

# File modes:

# Character	Meaning
# 'r'	    open for reading (default)
# 'w'	    open for writing, truncating the file first
# 'x'	    create a new file and open it for writing
# 'a'	    open for writing, appending to the end of the file if it exists
# 'b'	    binary mode
# 't'	    text mode (default)
# '+'	    open a disk file for updating (reading and writing)


# Writelines 
f = open("python/example.txt", "w")  # Open a file in write mode
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]  # List of lines to write to the file
f.writelines(lines)  # Write the list of lines to the file
f.close()  # Close the file

print("** Basic Read function **")
# read
f = open("python/example.txt", "r")  # Open a file in read mode
content = f.read()  # Read the entire content of the file
print(content)  # Print the content of the file
f.close()  # Close the file

print("** Readline, Readlines, tell and seek functions **")
# Readlines
f = open("python/example.txt", "r")  # Open a file in read mode
print(f.readline()) # Read and print the first line of the file
print(f.tell())  # Get the current position of the file pointer
f.seek(0)  # Move the file pointer to the beginning of the file
lines = f.readlines()   # Read all lines into a list
for line in lines:  # Iterate through the list of lines
    print(line.strip())  # Print each line without leading/trailing whitespace
f.close()  # Close the file

print("** Using Context Manager **")
# Using Context Manager (with statement)
with open("python/example.txt", "r") as f:
    content = f.read()  # Read the entire content of the file
    print(content)  # Print the content of the file

# What is context manager?
# A context manager is a Python construct that allows you to manage resources, such as file handling, in a clean and efficient way. It ensures that resources are properly acquired and released, even if an error occurs during the execution of the code block. The most common way to use a context manager is with the `with` statement, which automatically handles opening and closing files.
# custom context manager (This is how the context manager works behind the scenes)

print("** Custom Context Manager **")
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)  # Open the file
        return self.file  # Return the file object

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()  # Close the file when exiting the context

# Using the custom context manager
with FileManager("python/example.txt", "r") as f:
    content = f.read()  # Read the entire content of the file
    print(content)  # Print the content of the file

#  Issue working with text files in Python
#  Can't work with binary files like images
#  not work for the int, float, complex, bool, list, tuple, set, dict, etc. data types

print("** Working with Binary Files **")
with open("python/test.png", "rb") as f:
    with open("python/test_copy.png", "wb") as f_copy:
        f_copy.write(f.read())  # Read the binary content of the image and write it to a new file

with open("python/example.txt", "w") as f:
    f.write(5)  # This will raise a TypeError because write() expects a string, not an integer

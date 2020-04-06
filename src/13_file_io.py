"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
file1 = open("foo.txt", "r")
contents = file1.read()
print(contents)
# print(file1)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
file2 = open("bar.txt", "w")
file2.write("line 1\n")
file2.write("line 2\n")
file2.write("line 3\n")

name = input("Whats your name? ")
file2.write(name)

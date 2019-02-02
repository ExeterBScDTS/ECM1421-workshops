# reading_files.py
# ECM1421 examples
# Michael Saunby

# Before we use a file, we must "open" it, like this:

my_file = open("words.txt")

# my_file is a variable of the Python type "stream"
# We've encountered streams before, but haven't assigned a stream
# to a variable.  The print() funtion use a stream in order to
# write to the console/terminal.

# If we print a stream variable we don't get the contents of the file.
print(my_file)

# There are many ways to read the contents of a file.
# For example.
first_line = my_file.readline()
print(first_line)

exit("stopping here")

# Or read all the lines, one at a time, with a for loop
for my_line in my_file:
    print(my_line)


print("Now try again...")
for my_line in my_file:
    print(my_line)
print("... and get nothing!  Files are not quite like lists.")

# Remove next line to run the rest of this example.
exit("stopping here")

# If we want a list we use readlines() method.
my_file = open("words.txt")
all_lines = my_file.readlines()
# An alternative style with the same result is
# all_lines = list(my_file)
# Use whichever style makes most sense to you.

# Just print a few lines...
for my_line in all_lines[0:5]:
    print(my_line.strip())

# And again...
for my_line in all_lines[0:5]:
    print(my_line.strip())

# Reading files does NOT take a long time.  It's
# actually the print() that takes time.
# e.g. we can count the lines like ths.
print("Count lines in file...")
my_file = open("words.txt")
count = 0
for my_line in my_file:
    count += 1
print("Counted " + str(count) + " lines.")

# When we've finished with a stream/file we should close it.
my_file.close()
print(my_file)

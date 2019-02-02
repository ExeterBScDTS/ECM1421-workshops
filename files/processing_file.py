# processing_files.py
# ECM1421 examples
# Michael Saunby

# As we saw in reading_files.py reading files does NOT take a long time.

print("Count lines in file...")
my_file = open("words.txt")
count = 0
for my_line in my_file:
    count += 1
print("Counted " + str(count) + " lines.")


# So lets define a function that will calculate the mean length of
# lines in a file.


def mean_length(my_file):
    count = 0
    mean = 0.0
    total = 0.0
    for my_line in my_file:
        count += 1
        # Re-calculate the mean for each line rather than keeping a total
        mean = (mean * (count-1) + len(my_line.strip())) / count
        # Maybe the algorithm isn't right? OK, let's total too!
        total += len(my_line.strip())
    return (mean, total/count)


# This will likely take less than 1 second!
print(mean_length(open("words.txt")))

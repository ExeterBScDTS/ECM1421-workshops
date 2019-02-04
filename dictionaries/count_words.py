# count_words.py
# ECM1421 examples
# Michael Saunby


def count_by_first( my_list ):
    """
    Count all the words in my_list and return a dict with with key of
    initial character and value of words counted with that initial.
    """
    counts_dict = {}
    for word in my_list:
        # get the first character of the string
        initial = word[0]
        # check if this key has already been added to the dict
        if initial in counts_dict:
            # it has so we can increment the count
            counts_dict[initial] += 1
        else:
            # it hasn't so we must initialise both key and value
            counts_dict[initial] = 1
    return counts_dict

# Test the function with a few words in a list
print(count_by_first(["ant","axe","bat","bee","bluff","zoo"]))

#exit("stop here")

# Now try again with a large file
file_name = "../files/words.txt"
words_file = open(file_name)

# Although a file (stream) is not a list Python can use a stream where
# a list is expected. Or use readlines() to convert to list.
print(count_by_first(words_file))

# Note that output has counts for 'A', 'a', 'B', 'b', etc.
# How would you change the function to combine counts for 'A' and 'a', etc?

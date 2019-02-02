# dictionary_example.py
# ECM1421 examples
# Michael Saunby

first_dict = {"first_name": "Michael", "full_name": "Michael Saunby"}

print(first_dict)
print(first_dict["full_name"])

first_dict["nick_name"] = "Mike"
print(first_dict)

# Note - did not need to use append() to add a new item.

# The are other differences from lists
for thing in first_dict:
    print(thing)

# Is probably not what we wanted, so use this...
for thing in first_dict.items():
    print(thing)

# Typically we would write this as...
for (key, value) in first_dict.items():
    print("Key is " + str(key) + ", value is " + value)

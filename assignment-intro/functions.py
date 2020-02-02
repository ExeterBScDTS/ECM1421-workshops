##
# Functions
##

# Some functions are already defined for us, like print()

print("hello")

# or len()

length_of_word = len("hello")

# Notice that we get a result from our function and use = to assign this to a variable,
# but we can ignore it.

len("hi")

# Why would we ignore the returned value?  Well sometimes it's what the function does
# that matters most, e.g. print()

# To define our own functions we use def

def first_function( a_value ):
    return a_value

# This function isn't very useful, it just returns the value it is given as an "argument"

a = first_function( 12 )
b = first_function( "some words" )
c = first_function( len([0,1,2,3,4]) )
d = first_function( [a,b,c] )

print("a", a)
print("b", b)
print("c", c)
print("d", d)

# Most functions do more than just copy their argument, but don't try to write functions
# that do a lot. Much better to break a big problem into smaller pieces.

def min_max( my_list ):
    my_min = min(my_list)
    my_max = max(my_list)
    return my_min, my_max

print( min_max( [3,6,7,-5,23] ) )

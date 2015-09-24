'''
LISTS
'''

# creating
a = [1, 2, 3, 4, 5]     # create lists using brackets

# slicing
a[0]        # returns 1 (Python is zero indexed)
a[1:3]      # returns [2, 3] (inclusive of first index but exclusive of second)
a[-1]       # returns 5 (last element)

# appending
a[5] = 6        # error because you can't assign outside the existing range
a.append(6)     # list method that appends 6 to the end
a = a + [7]     # use plus sign to combine lists

# sorting
sorted(a)               # sorts the list
sorted(a, reverse=True) # reverse=True is an 'optional argument'
sorted(a, True)         # error because optional arguments must be named

# checking type
type(a)     # returns list
type(a[0])  # returns int

# checking length
len(a)      # returns 7


'''
STRINGS
'''

# creating
a = 'hello'     # can use single or double quotes

# slicing
a[0]        # returns 'h' (works like list slicing)
a[1:3]      # returns 'el'
a[-1]       # returns 'o'

# concatenating
a + ' there'        # use plus sign to combine strings
5 + ' there'        # error because they are different types
str(5) + ' there'   # cast 5 to a string in order for this to work

# uppercasing
a[0] = 'H'      # error because strings are immutable (can't overwrite characters)
a.upper()       # string method (this method doesn't exist for lists)

# checking length
len(a)      # returns 5 (number of characters)


'''
FOR LOOPS AND LIST COMPREHENSIONS
'''

# for loop to print 1 through 5
nums = range(1, 6)      # create a list of 1 through 5
for num in nums:        # num 'becomes' each list element for one loop
    print num

# for loop to print 1, 3, 5
other = [1, 3, 5]       # create a different list
for x in other:         # name 'x' does not matter
    print x             # this loop only executes 3 times (not 5)

# for loop to create a list of cubes of 1 through 5
cubes = []                  # create empty list to store results
for num in nums:            # loop through nums (will execute 5 times)
    cubes.append(num**3)    # append the cube of the current value of num

# equivalent list comprehension
cubes = [num**3 for num in nums]    # expression (num**3) goes first, brackets
                                    # indicate we are storing results in a list
# EXERCISE:
# 1. Given that: letters = ['a','b','c']
# Write a list comprehension that returns: ['A','B','C']
# 2. Given that: word = 'abc'
# Write a list comprehension that returns: ['A','B','C']
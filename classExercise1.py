# strings
str()
# intergers
int()
# floats
float()

# print function, this prints hallo world
print('hello world')

# variables
hello = 'hello'

world = 'world'

print(hello, world)

print('I am printing ', hello, world, '!')

# or

# use placeholders
# this might look more complicated then it actually is but when strings get much bigger its much more simple then the above example
print('I am printing %s %s!' % (hello, world))


# lists and stings

# list
# the list is numbered(indexed) like the following
#       0  1  2  3  4
list = [1, 2, 3, 4, 5]

# string
# the string is numbered like the following
#         01234
string = "12345"

# to prove that string and lists are similar
print(list[2])
print(int(string[2]))  # here we are converting the the string answer to an interger to give the same output as above

"""
This is where the exercise starts.
your challenge is to fill in the areas with question marks (?)
and please if you get stuck put your hand up
"""

## Question 1.

# if statements

"""
In this question i want you to replace the question marks (?) with either 'the colour is equal to red' or 'the colour is not equal to red'' 
"""

colour = "red"

if colour == "red":
    print("?")
else:
    print("?")

## Question 2.

name = input("enter your name: ")

"""
here i want to check if the first character in the name entered by the user (this is initialised up above) is m
if there name starts with m print "your name starts with m" if not then print "your name dose not start with m"
also note that you must replace the (?) inside the square brackets [] with the appropriate index to only get the first letter
"""

if name[0] == "m" or name[0] == "M":
    print("Your name starts with m")
else:
    print("Please leave")

## Question 3.

# for loops

mylist = [1, 3, 5, 7, 9]

"""
here i want you to irritate though the list given above, replace the ? with the correct word/variable
"""

for item in mylist:
    print(?)



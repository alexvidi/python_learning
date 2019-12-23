# To RUN a Python script file (.py) just run `python yourfilename.py` on your terminal

# COMMENTS in Python
# this is a comment

''' this is a
multiline comment
'''

""" this is also
a
multiline comment"""

# VARIABLE TYPES

# Strings
# in python can be expressed with single and double quotes, so:
label = "This is a string"
# is the same as
label = 'This is a string'

# OUTPUT using the print function
print("Hello World!")  # print hello world
name = "Alex"
print("Hello " + name)  # print hellow name

# Numbers
# next are integers
zero = 0
one = 1
two = 2
three = 3
# next are floats
a = 0.5
b = 1.0
c = 3.2

# you can make operations with this numbers
print("zero + one - two * three = ", zero + one - two * three)
# also with floats (** is power operator)
print("a + b - c * two ** three = ", a + b - c * two ** three)

# Booleans
is_number = False
is_string = True

# Lists
l = []  # empty list
li = [0, 1, 2, 3]  # integer list
lo = ["a", "b", "c", "d"]  # string list
# to add elements into a list
l.append(a)
l.append(b)
l.append(c)
# list can be accessed by index value
print("li[2] = ", li[2])
print("lo[1] = ", lo[1])

# Tuples
tup = (0, "game", True, 3, "PYTHON")
print("tup[2] = ", tup[2])  # they can also be accessed by index value

# Dictionaries
dic = {}  # empty dictionary
dic["key"] = "value"  # add a key-value pair into the dictionary
# they can also be filled this way
dic_0 = {
    "name": "Alex",
    "surname": "Vidal",
    "age": 29,
    "gender": "male",
    "isMale": True
}
# dict values can be accessed by key as index
print("name: ", dic_0["name"])

# all variable types can be checked using the built-in function "type"
print(type(dic))
print(type(tup))
print(type(l))
print(type(a))
print(type(one))
print(type(label))

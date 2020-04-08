#!/usr/bin/env python
# coding: utf-8

# ### First steps in Pyhton

# To RUN a Python script file (.py) just run `python yourfilename.py` on your terminal

# __COMMENTS in Python__

# In[2]:


# this is a comment

''' this is a
multiline comment
'''

""" this is also
a
multiline comment"""


# __VARIABLE TYPES__

# Strings

# In[7]:


# in python can be expressed with single and double quotes, so:
label = "This is a string"

# is the same as
label = 'This is a string'

# OUTPUT using the print function
print("Hello World!")  # print hello world

name = "Alex"

print("Hello " + name)  # print hello name
print("Hello", name)  # same, using two arguments
print(f"Hello {name}!")  # same without + concatenation


# __Numbers (integers and floats)__

# In[8]:


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
print(f"a + b - c * two ** three = {a + b - c * two ** three}")


# __Booleans__

# In[3]:


is_number = False
is_string = True

if is_number:
    print("It is a number!")
else:
    print("It is NOT a number!")

print(is_number)
is_string


# __Lists__

# In[13]:


l = []  # empty list
li = [0, 1, 2, 3]  # integer list
lo = ["a", "b", "c", "d"]  # string list

# to add elements into a list
l.append(a)
l.append(b)
l.append(c)

# list can be accessed by index value
print(f"li[2] = {li[2]}")
print(f"lo[1] = {lo[1]}")


# __Tuples__

# In[15]:


tup = (0, "game", True, 3, "PYTHON")
print("tup[2] =", tup[2])  # they can also be accessed by index value


# __Dictionaries__

# In[17]:


dic = {}  # empty dictionary
dic["key"] = "value"  # add a key-value pair into the dictionary

# they can also be filled this way
dic_new = {
    "name": "Alex",
    "surname": "Vidal",
    "age": 29,
    "gender": "male",
    "isMale": True
}

# dict values can be accessed by key as index
print(f"name: {dic_new['name']}")


# __Check variable types__

# In[18]:


# all variable types can be checked using the built-in function "type"
print(type(dic))
print(type(tup))
print(type(l))
print(type(a))
print(type(one))
print(type(label))


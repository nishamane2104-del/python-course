# python list : allows to store multiple items in a single variable. Lists are ordered, changeable, and allow duplicate values. They are defined using square brackets [] and can contain elements of different data types.
L = [1, 2, 3, "nisha", 4.5, True]  #integer(0), integer(1), integer(2), string(4), float(5), boolean(6)
print (L)
# characteristics of python list
# 1. Lists are ordered: The items in a list have a defined order, and that order will not change unless we explicitly modify the list. We can access items in a list using their index, which starts at 0.
# 2. Lists are changeable (mutable): We can modify a list after it has been created. This means we can add, remove, or change items in a list.
# 3. Lists allow duplicate values: A list can contain multiple items with the same value. Each occurrence of the value is treated as a separate item in the list.
# 4. Lists can contain different data types: A list can contain items of different data types, including integers, floats, strings, booleans, and even other lists.
# 5. Lists are dynamic: We can add or remove items from a list, and the list will automatically adjust its size to accommodate the changes.

myfirst = [1, 2, 3, "nisha", 4.5, True]
# changing the element of the list
myfirst[3] = "aniket"
print(myfirst)
# adding an element to the list
myfirst.append("python")
print(myfirst)
# removing an element from the list
myfirst.remove(4.5)
print(myfirst)
# inserting an element at a specific position
myfirst.insert(2, "new element")
print(myfirst)
# accessing elements of the list
print(myfirst[0])  # first element
print(myfirst[3])  # fourth element
print(myfirst[-1]) # last element 
# creating duplicate values in the list
dup1st = [1, 2, 5, 6, 3, 2, 1, 3, 4, 5, 15, 12, 15, 1]
print(dup1st)

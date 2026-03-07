# Operations on list: there are many operations that can be performed on lists in Python, including adding, removing, and modifying elements, as well as slicing and concatenating lists. Here are some common operations on lists:

# creating a list
empty_list = []  # an empty list
numbers = [21, 2002, 20, 1999] # integers
mixed = [21, "nisha", 4.5, True] # mixed data types
print(empty_list)
print(numbers)
print(mixed)

#accessing list elements
mylist = [1, 2, 3, "nisha", 4.5, True]
print(mylist[0])  # first element
print(mylist[3])  # fourth element
print(mylist[-1]) # last element

# adding elements append = adds an element to the end of the list, insert = adds an element at a specific position, extend = adds elements from another list to the end of the list
list = [4, 2, 7, 9, 2002]
list.append (15) #adding
print(list)
list.insert(2, 10) #inserting
print(list)
list.extend([1, 3, 5]) #extending
print(list)

# updating elements
mylist = [55, True, "reva", 333]
mylist[0] = 125649730
print(mylist)

#removing elements : remove(value) = removes the first occurence of the value, 
# pop(index): removes the element at a specifuc index 
# del statement: deletes an element or the entire list
mylist = [55, True, "reva", 333]
mylist.remove(True)  # removes the first occurrence of True
print(mylist)
mylist.pop(1)  # removes the element at index 1
print(mylist)
del mylist[1]  # deletes the element at index 1
print(mylist)

#iterating over list
mylist = [12, 24, 36, 48, 60]
print("Iterating using for loop:")
#Using for loop 
for ele in mylist:
    print(ele)
print("\nIterating using while loop:")
#Using while loop
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1  

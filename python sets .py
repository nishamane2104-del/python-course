# python sets
#In Python, a Set is one of the four built-in data types used to store numerous items in a single variable. Set is an unindexed and unordered collection of unique elements. For example, a set is suitable option when storing information about employee IDs as these IDs cannot have duplicates.
# creating a Set
S = {2202, 205, 3994, 7398}
print(S)

#characteristics of python sets
# unordered: sets do not maintain the order of how elements are stored in them 
# unindexed: we cannot access the data elements of sets
# No Duplicate Elements: Each data element in a set is unique 
# mutable (Changeable): Sets in Python allow modifications of their elements after creation  

# Creating a set in Python is quite simple and easy process. Python offers two ways to create a set:
# Using curly braces
int_set = {12, 6, 7, 9, 11, 10}   # set of integers  
print(int_set)  
  
str_set = {'one', 'two', 'three', 'four', 'five'} # set of strings  
print(str_set)  
  
mixed_set = {12, 'tpointtech', 7.2, 6e2} # mixed set  
print(mixed_set) 

# Using the Set() function
# given list  
int_list = [6, 8, 1, 3, 7, 10, 4]  
  
# creating set using set() function  
int_set = set(int_list)  
  
print("Set 1:", int_set)  
  
# creating an empty set  
empty_set = set()  
  
print("Set 2:", empty_set) 

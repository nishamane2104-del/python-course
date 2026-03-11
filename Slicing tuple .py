# slicing in tuple : slicing is a powerful technique in Python that allows you to extract a portion of a sequence, such as a tuple, by specifying a range of indices. 
# The syntax for slicing is as follows: sequence[start:stop:step]. 
# Here, start is the index where the slice begins (inclusive), stop is the index where the slice ends (exclusive), and step is the interval between indices (optional).
# Here are some examples of slicing tuples:

# creating a tuple
mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Elements between indices 1 and 5:", mytuple[1:5])  # slicing from index 1 to 4 (5-1)
print("Elements from the beginning to index 4:", mytuple[:5])  # slicing from the beginning to index 4 (5-1)
print("Entire tuple:", mytuple)

#deleting a tuple (del tuple_name)
sampletuple = ("Apple", "Mango", "Banana", "Orange")
print("Given Tuple:", sampletuple)
try: 
    del sampletuple[3]
    print(sampletuple)
except Exception as e:
    print(e)
# deleting the variable from the global space of the program using del keyword
del sampletuple
try:
    print (sampletuple)
except Exception as e: 
    print(e)

# changing the elements in Tuple
fruit1 = ("mango", "orange", "banana", "apple")
print("Before changing the element in Tuple..")
print("Tuple=", fruit1)
# converting tuple into the list
fruitlist = list(fruit1)
#changing the element of the list
fruit2 = "grapes"
print ("Converting",  fruit2, "-", fruitlist)
# converting the list back into the tuple
fruit1 = tuple(fruitlist)
print("After changing the Element in Tuple..")
print("Tuple=", fruit1)

# adding elements into a list
# Step 1: Convert the Tuple into a List.
# step 2: Add the required element to the list using the append() method.
#Step 3: Convert the List back into the Tuple.
fruits_tuple = ("mango", "orange", "banana", "apple")
# printing tuple before update 
print("Before Adding a new elemet in Tuple...")
print("Original tuple =", fruits_tuple)
#converting the tuple into the list
fruits_list = list(fruits_tuple)
#changing the element of the list
fruits_list.append("blueberry")
print("Adding New Element -> 'blueberry'")
#converting the list back into the tuple
fruits_tuple = tuple(fruits_list)
# printing the tuple after update 
print("After adding a new element in Tuple..")
print ("Updated Tuple =", fruits_tuple)

#adding a tuple to tuple
# Step 1: Create a new Tuple with the element(s) we want to add.
# Step 2: Adding the new tuple to the existing tuple.
fruits_tuple=("banana", "mango", "orange", "papaya")
# printing the tuple before update
print("Before Adding a New Element in Tuple...")  
print("Original Tuple =", fruits_tuple)    
# creating a new tuple consisting new element(s)  
temp_tuple = ("pineapple", )  
# adding the new tuple to the existing tuple  
# fruits_tuple = fruits_tuple + temp_tuple  
fruits_tuple += temp_tuple  
# printing the tuple after update  
print("Adding New Element -> 'pineapple'")  
print("After Adding a New Element in Tuple...")  
print("Updated Tuple =", fruits_tuple)  
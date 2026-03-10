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
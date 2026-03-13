# unpacking tuples
# creating a tuple (Packing a Tuple)  
fruits_tuple = ("mango", "orange", "banana", "apple", "papaya")  
# printing the given tuple for reference  
print("Given Tuple :", fruits_tuple)   
# unpacking a tuple  
(varOne, varTwo, varThree, varFour, varFive) = fruits_tuple  
# printing the results  
print("First Variable :", varOne)  
print("Second Variable :", varTwo)  
print("Third Variable :", varThree)  
print("Fourth Variable :", varFour)  
print("Fifth Variable :", varFive)  

#looping tuples : using "for" and "while" loop
# creating a tuple  
fruits_tuple = ("mango", "orange", "banana", "apple", "papaya")  
# printing the given tuple for reference  
print("Given Tuple :", fruits_tuple)  
  
print("Looping with 'for' Loop:")  
i = 1  
# iterating through the tuple  
for fruit in fruits_tuple:  
    # printing the element  
    print(i, "-", fruit)  
    i += 1  
  
print("\nLooping with 'while' Loop:")  
# initializing an iterable with 0  
j = 0  
# using the while loop to iterate through the tuple  
while j < len(fruits_tuple):  
    # printing the element of the tuple  
    print(j + 1, "-", fruits_tuple[j])  
    # incrementing the index value by 1  
    j += 1  

# tuple operations in python 
# creating a tuple for concatenation  
vegetables_tuple = ('Potato', 'Tomato', 'Onion')  
# printing the tuple  
print("Vegetables Tuple =>", vegetables_tuple)  
  
# creating another tuple for concatenation  
fruits_tuple = ('Mango', 'Apple', 'Orange')  
# printing the tuple  
print("Fruits Tuple =>", fruits_tuple)  
  
# concatenating the tuples using the + operator  
tuple_of_food_items = vegetables_tuple + fruits_tuple  
# printing the resultant tuple  
print("Concatenated Tuple: Tuple of Food Items =>", tuple_of_food_items)  
  
# creating a tuple for repetition  
sampleTuple = ('Mango', 'Grapes', 'Banana')  
  
# printing the original tuple  
print("Original tuple =>", sampleTuple)  
  
# Repeating the tuple elements for 4 times using the * operator  
sampleTuple = sampleTuple * 4  
  
# printing the new tuple  
print("New tuple =>", sampleTuple)  
  
# creating a tuple for membership  
test_tuple = (12, 23, 35, 76, 84)  
# printing the tuple  
print("Given tuple =>", test_tuple)  
  
# test cases  
n = 35  
m = 47  
  
# checking whether variable n and m belongs to the given tuple or not using the membership operator  
if n in test_tuple:  
    print("Yes.", n, "is present in the tuple", test_tuple)  
else:  
    print("No.", n, "is NOT present in the given tuple.")  
  
if m in test_tuple:  
    print("Yes.", m, "is present in the tuple", test_tuple)  
else:  
    print("No.", m, "is NOT present in the given tuple.")  

# Tuple methods in Python : count(), index(), max(), min()
# count syntax : tuple_name.count(item)
# creating tuples  
T1 = (0, 2, 3, 6, 4, 2, 5, 6, 3, 2, 2, 6, 7, 2, 7, 8, 0, 1, 9, 1)  
T2 = ('Apple', 'Orange', 'Mango', 'Apple', 'Banana', 'Mango', 'Mango', 'Orange', 'Mango', 'Apple')  
# counting the occurrence of 2 in the tuple T1  
resultOne = T1.count(2)    
# counting the occurence of 'Mango' in the tuple T2  
resultTwo = T2.count('Mango')  
# printing the results  
print("Tuple T1 =>", T1)  
print("Total Occurrence of 2 in T1 =>", resultOne)  
# printing the results  
print("\nTuple T2 =>", T2)  
print("Total Occurrence of 'Mango' in T2 =>", resultTwo) 

# index syntax: tuple_name.index(item)
# creating tuples  
T1 = (0, 2, 3, 6, 4, 2, 5, 6, 3, 2, 2, 6, 7, 2, 7, 8, 0, 1, 9, 1)  
T2 = ('Apple', 'Orange', 'Mango', 'Apple', 'Banana', 'Mango', 'Mango', 'Orange', 'Mango', 'Apple')  
  
# searching for the occurrence of 2 in the tuple T1  
resultOne = T1.index(2)  
resultTwo = T1.index(2, 5)  
  
# searching for the occurence of 'Mango' in the tuple T2  
resultThree = T2.index('Mango')  
resultFour = T2.index('Mango', 3)  
  
# printing the results  
print("Tuple T1 =>", T1)  
print("First Occurrence of 2 in T1 =>", resultOne)  
print("First Occurrence of 2 after 5th index in T1 =>", resultTwo)  
  
# printing the results  
print("\nTuple T2 =>", T2)  
print("First Occurrence of 'Mango' in T2 =>", resultThree)  
print("First Occurrence of 'Mango' after 3rd index in T2 =>", resultFour)  

#max() syntax: max(object)
# creating a tuple  
sampleTuple = (5, 3, 6, 1, 2, 8, 7, 9, 0, 4)   
# printing the tuple for reference  
print("Given Tuple =>", sampleTuple)   
# using the max() method to find the largest element in the tuple  
largest_element = max(sampleTuple)   
# printing the result for the users  
print("The Largest Element in the Given Tuple =>", largest_element)  

# min() syntax: min (object)
# creating a tuple  
sampleTuple = (5, 3, 6, 1, 2, 8, 7, 9, 0, 4)    
# printing the tuple for reference  
print("Given Tuple =>", sampleTuple)   
# using the min() method to find the smallest element in the tuple  
smallest_element = min(sampleTuple)   
# printing the result for the users  
print("The Smallest Element in the Given Tuple =>", smallest_element)  
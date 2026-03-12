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


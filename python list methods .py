# append() = adds an element to the end of the list
list_of_fruits = ['apple', 'mango', 'banana', 'orange', 'guava']  
# printing the list  
print("List of Fruits:", list_of_fruits)  
# using the append() method  
list_of_fruits.append('grapes')  
# printing the updated list  
print("Updated List of Fruits:", list_of_fruits)  

# extend() = adds elements from another list to the end of the list
shopping_list = ['milk', 'bread', 'butter']  
new_items = ['eggs', 'apples', 'coffee']  
# printing the lists  
print("Old Shopping List:", shopping_list)  
print("New Items:", new_items)  
# using the extend() method  
shopping_list.extend(new_items)   
# printing the updated list  
print("Updated Shopping List:", shopping_list) 

#insert() = adds an element at a specific position
colors = ['red', 'green', 'blue']
print("Original List:", colors)
# using the insert() method to add 'yellow' at index 1
colors.insert(1, 'yellow')
print("Updated List:", colors)  

# remove() = removes the first occurrence of the value
numbers = [1, 2, 3, 4, 5, 2, 6]
print("Original List:", numbers)
# using the remove() method to remove the first occurrence of 2
numbers.remove(2)
print("Updated List:", numbers)

# pop() = removes the element at a specific index
mylist = ['a', 'b', 'c', 'd', 'e']
print("Original List:", mylist)
# using the pop() method to remove the element at index 2
removed_element = mylist.pop(2)
print("Removed Element:", removed_element)
print("Updated List:", mylist)  

# clear() = removes all the elements from the list
mylist = ['x', 'y', 'z']
print("Original List:", mylist)
# using the clear() method to remove all elements  
mylist.clear()
print("Updated List:", mylist)

# index() = returns the index of the first occurrence of the value
mylist = ['apple', 'banana', 'cherry', 'date', 'banana']
print("List:", mylist)
# using the index() method to find the index of the first occurrence of 'banana'
index_of_banana = mylist.index('banana')
print("Index of 'banana':", index_of_banana)    

# count() = returns the number of occurrences of the value
mylist = ['cat', 'dog', 'cat', 'bird', 'cat']
print("List:", mylist)
# using the count() method to count the occurrences of 'cat'
count_of_cat = mylist.count('cat')  
print("Count of 'cat':", count_of_cat)

# sort() = sorts the list in ascending order
numbers = [5, 2, 9, 1, 5, 6 ]   
print("Original List:", numbers)
# using the sort() method to sort the list
numbers.sort()
print("Sorted List:", numbers)  

# reverse() = reverses the order of the list
mylist = [1, 2, 3, 4, 5]
print("Original List:", mylist) 
# using the reverse() method to reverse the list
mylist.reverse()
print("Reversed List:", mylist)

# copy() = creates a shallow copy of the list
original_list = [10, 20, 30, 40]
# using the copy() method to create a copy of the original list
copied_list = original_list.copy()
print("Original List:", original_list)
print("Copied List:", copied_list)


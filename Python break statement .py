# In Python, the break is a keyword used to prematurely exit a loop, before the loop iterates through all the elements or met its condition. 
# Loop through numbers from 1 to 10    
for num in range(1, 11):    
    if num == 8:  
        break  # breaking the loop at 6  
    print(num)  
# Example 1: Break Statement with for Loop
fruits = ["apple", "banana", "cherry", "date", "fig"]
# using the for loop to iterate the the list 
for index, fruit in enumerate(fruits): 
    if fruit == "fig":
        print("Fruit found!")
        break 
print("located at index =", index)

# Example 2: Break Statement with while Loop
count = 21
while True:
    print ("Count:", count)
    if count == 27:
        print ("Condition met! Exiting loop.")
        break 
    count += 1

# Example 3: Break Statement with Nested Loop
# Innermost Loop Exit: A break statement will only exit the loop in which it is directly placed.
# Exiting Multiple Loops: In order to exit multiple levels of nested loops, we need to use additional strategies like adding flags, or encapsulating loops within functions.
matrix = [  
    [10, 15, 20],  
    [25, 30, 35],  
    [40, 45, 50]  
]  
# element to be searched  
target = 30  
  
found = False  # Flag to track if the number is found  
  
# using the for nested loop  
for row in matrix:  
    for num in row:  
        # if the current element is equal to the target value, set flag to True and break the loop        
        if num == target:  
            print(f"Number {target} found! Exiting loops.")  
            found = True  
            break  # using break statement  
    # exiting the outer loop  
    if found:  
        break  
# tables till 99 
for i in range(1, 10):
    for j in range(1, 10):
        if i * j > 50:
            break
        print(f"{i} x {j} = {i * j}")
# print 1 - 99 tables using loop
for i in range(1, 10):
    for j in range(1, 10):
        if i * j > 99:
            break
        print(f"{i} x {j} = {i * j}")
# print tables from 1 to 99 using loop 
for i in range(1, 100):
    for j in range(1, 100):
        if i * j > 1000:
            break
        print(f"{i} x {j} = {i * j}")
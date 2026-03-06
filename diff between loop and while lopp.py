# for loop syntax in python (for var_name in sequence)
#let's  print numbers in a for loop using Range()  
for i in range(1,27): #Here we have used for loop  
    print (i)   

# use if range() with for loop
#receiving the input from the users  
row = int(input("Enter number of rows: "))  
#using the range function in a For Loop  
for i in range(1, row + 1):  
    # Print spaces  
    for j in range(row - i): #nested loop used  
        print("  ", end="")  
      
    # Print stars  
    for stars in range(2 * i - 1):    
        print("* ", end="")  
      
    print()    

#while condition: (code block)
# initializing a counter variable    
counter = 0    
# using the while loop to iterate the counter up to 5    
while counter < 5:    
  # printing the counter value and some statement    
  print(counter, "Hello")    
  # incrementing the counter value    
  counter += 1 
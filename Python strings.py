#python on string
sample_string = "Python is a great programming language."
print(sample_string)
print("Data tyoe:", type(sample_string))
# characteristics of string
# 1. Strings are immutable: Once a string is created, it cannot be modified. Any operation that seems to modify a string will actually create a new string.
# 2. Strings are ordered: The characters in a string have a specific order, and we can access them using indexing and slicing.
# 3. Strings are iterable: We can iterate over the characters in a string using a loop.
# 4. Strings support various operations: We can concatenate strings, repeat them, and perform various other operations using built-in string methods.
# 5. Strings can contain any characters: A string can contain letters, numbers, symbols, and even whitespace characters.        
# We can create strings using either single quotation marks ('…') or double quotation marks ("…").
string1 = 'Hello, World!'  # Using single quotes
string2 = "Hello, World!"  # Using double quotes
print(string1)
print(string2)  
# In case we want a string to span multiple lines, then we can make use of triple quotation marks ('''…''' or """…""").
str1 = '''Learning python 
is fun 
with Nisha'''
str2 = """ I can teach 
anyone python 
very easily"""
print("Multiline String 1:")
print(str1)
print()
print("Multiline String 2:")
print(str2) 
# python program to access characters in a string  
# given string  
s = "Tpoint Tech"  
print("Given String:", s)  
# accessing characters using indexing  
print("s[0] =", s[0])  
print("s[9] =", s[9])
# python program to access characters from back of the string  
# given string  
s = "Tpoint Tech"  
print("Given String:", s)  
# accessing characters using negative indexing  
print("s[-1] =", s[-1])  
print("s[-6] =", s[-6])  
# string slicing
s = "Nisha tech"
print ("given string:", s)
# slicing from index 1 to 4 (5-1)
print("s[1:5]=", s[1:5])
# slicing from index 0 to 4 (5-1)
print("s[:5]=", s[:5])  
# getting characters from index 3 to the end of the string
print("s[3:]= ", s[3:])     
# reversing a string
print("s[::-1] =", s[::-1])
#string immutability
msg = "nishamane"
print("Given string:", msg)
#msg[0] = "N" # This will raise an error because strings are immutable
# To change the string, we need to create a new string
msg = "N" + msg[1:5] + "M" + msg[6:]
print("New String:", msg)
# deleting a string
msg = "This string will be deleted"
print("Before deletion:", msg)  
del msg
# print(msg) # This will raise an error because the string has been deleted
# python program to update a string  
# given string  
given_str = "welcome learners"  
print("Given String:", given_str)  
# updating a string by creating a new one  
new_str_1 = "W" + given_str[1:]  
# replacing "learners" with "to Tpoint Tech"  
new_str_2 = given_str.replace("learners", "to Tpoint Tech")  
# printing results  
print("New String 1:", new_str_1)  
print("New String 2:", new_str_2) 
# common string operations
# len() function  
# given string  
given_str = "tpointtech"  
print("Given String:", given_str)  
# using the len() function  
num_of_chars = len(given_str)  
print("Number of Characters:", num_of_chars)  
#upper() and lower()
# given string  
given_str = "Tpoint Tech"  
print("Given String:", given_str)  
# using the upper() method  
print("Uppercase String:", given_str.upper())  
# using the lower() method  
print("Lowercase String:", given_str.lower()) 
#strip() and replace()
# given string  
str_1 = "      Nisha    "  
print("String 1:", str_1)  
# removing spaces from both ends  
print("After removing spaces from both ends:")  
print(str_1.strip())  
str_2 = "Learning Python with Nisha is fun!"  
print("String 2:", str_2)  
# replacing 'fun' with 'amazing'  
print("After replacing 'fun' with 'amazing':")  
print(str_2.replace("fun", "amazing"))  
# String Concatenation and Repetition
# given string  
str_1 = "Nisha"  
str_2 = "Biotech"  
# CONCATENATION: using the + operator  
str_3 = str_1 + " " + str_2  
print("Concatenated String:", str_3)  
# REPETITION: using * operator  
str_4 = str_1 * 4  
print("Repeated String:", str_4)  
#Using f-strings
name=("Reva")
age=("2")
city=("Panchgani")
# using f-strings to format the string
print(f'{name} is a {age} year old girl from {city}.')
# format()
name = "Gaurangi"
profession = "Student"
school = "SJC"
# using the format() method to format the string
msg = "{} is a {} at {}," .format(name, profession, school)
print(msg)
# string membership test
#given string
given_str = "Nisha is a biotechnologist"
# using in and not in keywords
print (f"does 'b' exist in '{given_str}'?", "b" in given_str)
print (f"does 'z' exist in '{given_str}'?", "z" in given_str)
print (f"does 'x' not exist in '{given_str}'?", "x" not in given_str)
print (f"does 'a' not exist in '{given_str}'?", "a" not in given_str)

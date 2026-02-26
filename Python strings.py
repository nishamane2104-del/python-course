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
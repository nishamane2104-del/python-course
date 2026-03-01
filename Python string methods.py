# Python String Methods to Change Case
# str.upper() - converts all characters in a string to uppercase
# str.lower() - converts all characters in a string to lowercase
# str.title() - converts the first character of each word to uppercase and the rest to lowercase
# str.capitalize() - converts the first character of the string to uppercase and the rest to lowercase
# str.swapcase() - converts uppercase characters to lowercase and lowercase characters to uppercase
str1 = str.upper("i am leaning python")
str2 = str.lower("I AM LEARNING PYTHON")
str3 = str.title("welcome to python leaning with nisha")
str4 = ("welcome to python leaning with nisha")
str5 = str.swapcase("I am Learning Python")
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
#Python String Methods to Search and Find Substrings
# str.find(substring) - returns the lowest index of the substring if found, otherwise returns -1
# str.rfind(substring) - returns the highest index of the substring if found, otherwise returns -1
# str.index(substring) - returns the lowest index of the substring if found, otherwise raises a ValueError
# str.rindex(substring) - returns the highest index of the substring if found, otherwise raises a ValueError
# str.count(substring) - returns the number of occurrences of the substring in the string
# str.startswith(substring) - returns True if the string starts with the specified substring, otherwise returns False
# str.endswith(substring) - returns True if the string ends with the specified substring, otherwise returns False
text = """ 
Now I will give you a proper notebook-writing structure that matches EXACTLY your university dissertation format — 
so whatever you write daily can directly be converted into your 
final hard-bound project.
Since your project is RNA-Seq analysis (PRJNA708303 – Homo sapiens), I’ll align everything according to your official structure.
"""  
  
index = text.find("structure")       # using find() method  
print(f"Index of 'structure': {index}")  
  
index = text.rfind("structure")      # using rfind() method  
print(f"Last index of 'structure': {index}")  
  
try:  
    index = text.index("analysis")    # using index() method  
    print(f"Index of 'analysis': {index}")  
except ValueError:  
    print("Substring 'analysis' not found.")  
  
try:  
    index = text.rindex("RNA-Seq")   # using rindex() method  
    print(f"Last index of 'RNA-Seq': {index}")  
except ValueError:  
    print("Substring 'learning' not found.")  
  
starts_with_now = text.startswith("Now") # using startswith() method  
print(f"Starts with 'Now': {starts_with_now}")  
  
ends_with_basics = text.endswith("basics.")   # using endswith() method  
print(f"Ends with 'basics.': {ends_with_basics}")  
  
count_tpoint = text.count("structure")     # using count() method  
print(f"Count of 'structure': {count_tpoint}")  

# Python String Methods to Split and Join Strings
# str.split(separator) - splits the string into a list of substrings based on the specified separator (default is any whitespace)
# str.rsplit(separator) - splits the string into a list of substrings based on the specified separator, starting from the right (default is any whitespace)
# str.splitlines() - splits the string at line breaks and returns a list of lines
# str.join(iterable) - joins the elements of an iterable (e.g., list) into a single string, with the specified string
sentence = "RNA-Seq is a powerful technique for transcriptome analysis."
split_str = sentence.split()
print(split_str)
rsplit_str = sentence.rsplit()
print("Right split string:", rsplit_str)
partition_str = sentence.partition("sample")
print("Partitioned string:", partition_str)
list_of_str = ["RNA-Seq", "is", "a", "powerful", "technique"]
joined_str = " ".join(list_of_str)
print("Joined string:", joined_str)
joined_str_comma = ",".join(list_of_str)
print("Joined string with comma:", joined_str_comma)
#Python String Methods to Validate Strings
# a function to validate the string  
def validate_string(input_str):  
  """Validates a string using various string methods."""  
  # printing the results  
  print(f"Given String: {input_str}")  
  print(f"Is alphabetic (str.isalpha()): {input_str.isalpha()}")  
  print(f"Is digit (str.isdigit()): {input_str.isdigit()}")  
  print(f"Is alphanumeric (str.isalnum()): {input_str.isalnum()}")  
  print(f"Is space (str.isspace()): {input_str.isspace()}")  
  print(f"Is lowercase (str.islower()): {input_str.islower()}")  
  print(f"Is uppercase (str.isupper()): {input_str.isupper()}")  
  print(f"Is titlecase (str.istitle()): {input_str.istitle()}")  
  print("-" * 30)  
# main function  
if __name__ == "__main__":  
  # calling the function to validate the string  
  validate_string("Welcome")  
  validate_string("PYTHON")  
  validate_string("Tpoint Tech")  
  validate_string(" ")  
  validate_string("hello friends")  
#Python String Methods for String Alignment and Formatting
# Using ljust(), rjust(), and center() for alignment  
text = "Tpoint"  
print(text.ljust(10, '-'))  # Left-align with '-' padding  
print(text.rjust(10, '-'))  # Right-align with '-' padding  
print(text.center(10, '-')) # Center-align with '-' padding  
  
# Using format() for string formatting with alignment  
name = "Morgan"  
age = 29  
print("My name is {:10} and I am {:3} years old.".format(name, age)) # Aligned with specified width  
  
# Using f-strings (formatted string literals) for alignment  
print(f"My name is {name:10} and I am {age:3} years old.")  
  
# Using zfill() for zero padding  
number = "1243"  
print(number.zfill(5))  # Pad with zeros to make it 5 characters long  
  
# Using format() with alignment specifiers for decimal places  
pi = 3.14159  
print("{:.2f}".format(pi)) # Format with 2 decimal places  
print("{:08.2f}".format(pi)) # Format with 2 decimal places and zero-padding up to 8 characters  
  
# Example of alignment with custom formatting  
string = "Tpoint"  
print(f"{string:^15}")  # Center align the string within 15 characters  
print(f"{string:<15}")  # Left align the string within 15 characters  
print(f"{string:>15}")  # Right align the string within 15 characters 
#python 
# hi python

# Type casting 
# Type casting is the process of converting a variable from one data type to another. In Python, we can use built-in functions like int(), float(), str(), etc. to perform type casting.    
# Two types of type casting:
# 1. Implicit type casting: This is done automatically by Python when we perform operations on different data types. For example, when we add an integer and a float, Python will automatically convert the integer to a float before performing the addition.
# 2. Explicit type casting: This is done manually by the programmer using built-in functions. For example, if we want to convert a string to an integer, we can use the int() function.
# Example of implicit type casting (int to float to complex)
a = 5   # integer
b = 7.8 # float
c = 3 + 4j # complex
d = a + b # implicit type casting to float
e = a + b + c # implicit type casting to complex
print(d, "=", type(d))
print(e, "=", type(e))

# Example of explicit type casting (integer conversion)
# explicit type casting
int1 = int(123.6) # float to integer
int2 = int("321") # string to integer
print(int1, "=", type(int1))
print(int2, "=", type(int2))
# python program to convert data type to Boolean  
# explicit type casting  
bool_1 = bool(0)    # int -> bool   
bool_2 = bool('')  # str -> bool  
bool_3 = bool('Tpoint Tech')  # str -> bool  
bool_4 = bool(14.5) # float -> bool  
bool_5 = bool([]) # list -> bool  
bool_6 = bool((1, 3, 5)) # tuple -> bool  
# printing results  
print(bool_1, "->", type(bool_1))  
print(bool_2, "->", type(bool_2))  
print(bool_3, "->", type(bool_3))  
print(bool_4, "->", type(bool_4))  
print(bool_5, "->", type(bool_5))  
print(bool_6, "->", type(bool_6))    

# python program to convert variables and values to strings  
# explicit type casting  
str_1 = str(5)  # int -> str  
str_2 = str(8.9) # float -> str  
str_3 = str(5 + 9j) # str -> str  
str_4 = str(True) # bool -> str  
# printing results  
print(str_1, "->", type(str_1))  
print(str_2, "->", type(str_2))  
print(str_3, "->", type(str_3))  
print(str_4, "->", type(str_4))   

# python program to convert variables and values to complex numbers  
# explicit type casting  
complex_1 = complex(5)  # int -> complex  
complex_2 = complex(8.9) # float -> complex  
# printing results  
print(complex_1, "->", type(complex_1))  # 0j is added  
print(complex_2, "->", type(complex_2))  

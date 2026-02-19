print("hello Aniket Shinde")
print("Welcome to Python Programming")
print("hello Aniket Shinde") 
#this is a comment
print("Welcome to Python Programming") 
def welcome(John):
    """This function welcomes the user to Python Programming"""
    print(f'hello {John}! Welcome to Python Programming')
    #calling the function
welcome("John")
print("Docstring:", welcome.__doc__)
#Using String Assignment and Print
msg = "hello Aniket Shinde"
print(msg)
#python variables
# Variable 'a' stores the integer value 17
a = 17
# Variable 'b' stores the string value "Python"
b = "Python"
print(a)
print(b)
# assigning multiple variables
var1 = var2 = var3 = "Python"
print("variable1:", var1)
print("variable2:", var2)
print("variable3:", var3)
#assigning different values to multiple variables
var1, var2, var3 = "nisha", "aniket", "python"
print("variable1:", var1)
print("variable2:", var2)
print("variable3:", var3)
#type casting a variable
var1 = 9
var2 = var1/5
print(var2)
var2 = int(var2)
print(var2)
var1 = 7.9
var2 = var1/3
print(var2)
var2 = int(var2)
print(var2)
#"Type" of variables
var_a = 5
var_b = "nisha"
var_c = 20.21
var_d = True
var_e = [4, "nisha", 20.21, True]
print(var_a,':', type(var_a))
print(var_b,':', type(var_b))
print(var_c,':', type(var_c))
print(var_d,':', type(var_d))
print(var_e,':', type(var_e))
#scope of variables
def make_tea():
    """This function makes tea"""
    print("Boil water")
    print("Add tea leaves")
    print("Add sugar")
    print("Stir well")
    print("Tea is ready!")
make_tea()
# global variable
global_var = 15

def add():
    local_var = 10   # 4 spaces before this line
    print(f'{global_var} + {local_var} = {global_var + local_var}')

add()

print("global_var =", global_var)
# print("local_var =", local_var)  # This will cause error
var_x = 13
def add():
    var_y = 16
    print(f'{var_x} + {var_y} = {var_x + var_y}')

add()
print("var_x =", var_x)
var1 = "nisha"
def meet():
    var2 = "aniket"
    print(f'{var1} meets {var2}')
meet()
print("var1 =", var1)
var1 = "Python is a programming language"
def hi():
    var2 = "and it is easy to learn"
    print(f'{var1} {var2}')
hi()
var_a = 15
print(var_a)

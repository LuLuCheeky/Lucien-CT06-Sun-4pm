#Prints
#Print is like this:
print("What you want to say?")
#Can also print numbers
print(699)
#or variables
num = "Hi!"
print(num)


#Types
#There are 3 types of code in Python
#String
#Integer and Float
#and Variables
#You can check the type of a variable with the type() function
num = "Hello World!"
num2 = 42
num3 = 3.14
print(type(num))
print(type(num2))
print(type(num3))


#Strings
#Strings are a sequence of characters
string = "Hello World!"
#Strings can be sliced
print(string[0:5])
print(string[6:])
#Strings can be concatenated
String1 = "Hello"
String2 = "World!"
print(String1 + " " + String2)
#Strings can be formatted
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")


#Integers and Floats
#Integers are whole numbers
num1 = 17
#Floats are decimal numbers
num2 = 3.14
#Integers and Floats can be added, subtracted, multiplied and divided
add1 = 15
add2 = 12
print(add1 + add2)
sub1 = 32
sub2 = 12
print(sub1 - sub2)
mul1 = 5
mul2 = 3
print(mul1 * mul2)
div1 = 10
div2 = 2
print(div1 / div2)


#Variables
#Variables can be a string, int or float
#They are used to store data
#Variables can be named anything but must start with a letter or underscore
#You can declare a variable like this:
num = "Im blue"
num2 = 15
num3 = 3.141592654
print(num)
print(num2)
print(num3)
#Variables can be changed
num = "Im not blue anymore"
print(num)


#Math functions in python
#PEMDAS is used for operations (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction)
#Parentheses ()
#Exponents **
#Multiplication *
#Division /
#Addition +
#Subtraction -
#You can use these in python
#Example of code that can be used in stores:
Price = 10
Quantity = 5
Total = Price * Quantity
print("Total: " + str(Total))
#Note: You cannot put dollars sign ($) for code


#For loops
#For loops are used to iterate over a sequence (list, tuple, dictionary, set, or string)
#Example of a for loop
for i in range(5):
    print("Hello World!")
#This will print "Hello World!" 5 times
#You can also use a for loop to print the words in a string one by one
string = "Hello World!"
for i in string:
    print(i)
#This will print each character in the string "Hello World!" one by one
#Another example of a for loop for range
for i in range(1, 10):
    print(i)
#This will print the numbers 1 to 9
#Note that the range function is exclusive of the last number
#If you want it to include the last number, you can do this:
for i in range(1, 11):
    print(i)
#This will print the numbers 1 to 10
#This is 
#You can also use a for loop to iterate over a list
my_list = [1, 2, 3, 4, 5]
for var in my_list:
    print(var)
#This will print each number in the list


#While loops
#While loops are used to execute a block of code as long as a condition is true
#Example of a while loop
count = 0
while count < 5:
    print("Hello World!")
    count += 1
#This will print "Hello World!" uncil the variable count is equal to 5
#You can also use a while loop to print the numbers 1 to 10
count = 1
while count <= 10:
    print(count)
    count += 1
#This will print the numbers 1 to 10
#To make a forever loop, you can do this:
count = 0
while True:
    print("Hello World!")
    if count == 5:
        break
    count += 1
#This will print "Hello World!" forever
#Note that I had to use a break else it would go on forever and evetually crash the program
#This can be useful in someways like a new year countdown 

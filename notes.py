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
#Some prints using string concatentation
name = input("What is your name? ")
brith = int(input("When were you born? "))
age = 2025 - brith
print("Hello " + name + "! You are " + str(age) + " years old this year.")


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
#one more thing: Mod
#Mod (or modulus) is used to get the remainder of a division
#Example of mod
num1 = 10
print(num1 % 3)
#This will print 1 since 10 divided by 3 is 3 with a remainder of 1
#You can also use the mod operator to check if a number is even or odd
#Example of checking if a number is even or odd
num = 10
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
#This will print "The number is even" since 10 is even


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
#This is also useful for something like a newyear countdown
for i in range(10, 0, -1):
    print(i)
print("Happy New Year!")
#This will print the numbers 10 to 1 and then print "Happy New Year!"
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
#This can be useful in someways like a new year countdown or something else
count = 10
while True:
    print(count)
    if count == 1:
        break
    count -= 1
print("Happy New Year!")


#If else and elifs
#Ifs
#Ifs can be used to check if a condition is true
#Example of an if statement
num = 10
if num == 10:
    print("The number is 10")
#This will print "The number is 10" since num is 10
#Elses
#Elses can be used to check if a condition is true when the if condition is false
#Example of an else statement
num = 10
if num == 5:
    print("The number is 5")
else:
    print("The number is not 5")
#This will print "The number is not 5" since num is not 5
#Elifs
#Elifs can be used to check if a condition is true when the if condition is false
#Example of an elif statement
num = 10
if num == 5:
    print("The number is 5")
elif num == 10:
    print("The number is 10")
else:
    print("The number is not 5 or 10") #Here the else has to be added in the end else if its not in the middle it could cancel off the elif


#Oops I fogot about inputs
#Inputs
#Inputs are used to get data from the user
#Example of an input
name = input("What is your name? ")
print("Hello " + name + "!")
#This will print "Hello <name>!" where <name> is the name entered by the user
#You can also use inputs to get numbers from the user too
#Example of an input with integers
num = int(input("Enter a number: "))
print("The number is " + str(num))
#This will print "The number is <num>" where <num> is the number entered by the user
#Lets make it more complex so that it also checks whether the number is even or odd using mod and if else
num = int(input("Enter a number to check if its a odd or even: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
#This will print "The number is even" or "The number is odd" depending on the number entered by the user


#Lists
#Lists are used to store multiple items in a single variable``


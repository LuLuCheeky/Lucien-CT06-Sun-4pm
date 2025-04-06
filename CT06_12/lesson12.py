# Lesson 12 - While Loops

# Recap 1: Multiples of 3 and 5
# Create a program to check if a number is both divisible by 3
# and 5.

# 1. Ask the user to input a number
# 2. Using the '%' operator, check if the number is both a
#    multiple of 3 and 5:
#     If true, print "The number is divisible by 3 and 5!"
# 3. Else, print "The number is not divisible by 3 and 5"


# NUM = int(input("What number? "))
# if NUM % 3 == 0 and NUM % 5 == 0:
#     print("The number is divisable by three and five.")
# else:
#     print("The number is not divisable by three and five.")

# Task 1: Introduction to while loop
# **Task 1a**:
# Due to a pandemic, the government placed a limit to the number
# of visitors a venue can have.

# Using a 'while' loop, create a program that will increase the
# number of visitors by 1 before printing out the number of
# visitors admitted, until number of visitors reaches 50.

# 1. Create a 'visitors' variable and assign '0' to it
# 2. While there is less than 50 visitors,
#     I. Increase the visitor count by 1
#     II. Print the visitor count

# (For Task 1b & 1c)
# Modify your program to account for the number of visitors
# already present at the venue, and the number of maximum visitors
# allowed for the following:

# **Task 1b**:
# Visitors already present: 18
# Max visitors allowed: 30

# **Task 1c**:
# Visitors already present: 4
# Max visitors allowed: 25
 
# visitors = 0

# while visitors < 50:
#     visitors = visitors + 1
#     print("Visitors:" + str(visitors))

# visitors = 18

# while visitors < 30:
#     visitors = visitors + 1
#     print("Visitors:" + str(visitors))


# visitors = 4

# while visitors < 25:
#     visitors = visitors + 1
#     print("Visitors:" + str(visitors))

# visitors = 0
# while True:
#     if visitors == 30:
#         print("There are 30 visitors.")
#         break
#     else:
#         print("There are" , str(visitors) , "visitors.")
#         visitors = visitors + 1

# Task 3: Order taking using while loop
# Using what you have learnt so far, code a program to take a
# customer's order.

# Declare a variable called 'order' and assign an empty string
# variable "" to it.

# Using a 'while' loop:
# 1. Ask the user to enter their order
# 2. For each order entered, concatenate to the 'order' variable.
# 3. Exit the 'while' loop if the user enters "end"
# 4. On program end, print out the customer's order.

# **Bonus**
# 1. Modify your code to remove the comma (",") that appears
#    either at the start or end of your sentence
# order = ""
# while True:
#     user = input("What would you like to order? ")
#     if user == "end":
#         break
#     order = order + user + ", "
#     print(order)
# print(order)

# Task 4: while... else
# The else condition will run when the loop exits normally.
# i.e. when the while condition is no longer true.

# Using 'else', create a program that will count from 10 to 1,
# before printing "Happy New Year!"

# **Task 4a**:
# Using a 'while' loop:
# 1. Print the numbers from 10 to 1
# 2. Once count reaches 1, use 'else' to print
#    "Happy New Year!"

# **Task 4b**:
# Now, modify your 'while' loop from Task 4a such that:
# 1. If the number is 5, 'break' out of the loop
# 2. Ensure your code has an 'else'

# Observe that "Happy New Year!" is no longer printed
num = 10
while True:
    num = num - 1
    
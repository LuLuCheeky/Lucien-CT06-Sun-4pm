# num = int(input("What number? "))
# num = num > 0
# if num:
#     print("The number you have inputed is positive.")
# else:
#     print("The number you have inputed is negative.")

# import random

# num = str(random.randint(1, 10))
# guess = input("Guess a number from 1 to 10. ")
# if not guess == num:
#     print("Wrong! 😡")
#     print("The answer was" , num , ".")
# else:
#     print("Congrats! 😎")

# num = input("What number do you want to check?")
# if num % 2 == 0:
#     print("The number you have inputed is even.")
# else:
#     print("The number you have inputed is odd.")

import random

password = input("What do you want the password to be? (Player 1) ")
guess = input("What do you think the password is? (Player 2) ")
if guess == password:
    
num = int(input("What number? "))
num = num > 0
if num:
    print("The number you have inputed is positive.")
else:
    print("The number you have inputed is negative.")

import random

hardness = int(input("What do you want the max number be? "))
num = str(random.randint(1, hardness))
guess = 0
while guess != num:
    guess = input("What do you think the random number (1 - " + str(hardness) + ") is? ")
    if not guess == num:
        print("Wrong! 😡")
    else:
        break
print("Congrats! 😎")
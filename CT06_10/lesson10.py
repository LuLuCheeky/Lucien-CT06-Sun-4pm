num = int(input("What number? "))
num = num > 0
if num:
    print("The number you have inputed is positive.")
else:
    print("The number you have inputed is negative.")

import random

num = str(random.randint(1, 10))


if not guess == num:
    print("Wrong! 😡")
else:
    print("Congrats! 😎")
import random

# v1 = random.randint(1, 6) 
# v2 = random.randint(1,6)
# v3 = random.randint(1,6)
# v1 = (v1 % 2) == 0
# v2 = (v2 % 2) == 0
# v3 = (v3 % 2) == 0
# yoshi = v1 == v2 == v3
# yoshi = str(yoshi)
# print("All number are even/odd" , yoshi + "1")

# hardness = int(input("What do you want the max number be? "))
# num = str(random.randint(1, hardness))
# guess = 0
# while guess != num:
#     guess = input("What do you think the random number (1 - " + str(hardness) + ") is? ")
#     if not guess == num:
#         print("Wrong! 😡")
#     else:
#         break
# print("Congrats! 😎")

applePrice = 1
apples = input("How many apples would you like to buy? ")
if apples > 10:
    print("You will get a 10% discount for buying that many! ")
    discountPrice = apples / 10
    print("You need to pay $" + discountPrice)
else:
    print("You need to pay $" + apples)
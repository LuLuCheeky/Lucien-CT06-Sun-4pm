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

# import random

# password = input("What do you want the password to be? (Player 1) ")
# guess = input("What do you think the password is? (Player 2) ")
# if guess == password:
#     print("Login successful.")
# else:
#     print("Loggin unsuccessful.")

# age = int(input("Whats ur age? "))
# if age < 13:
#     print("You are a child.")
# elif age > 20:
#     print("You are teen. ")
# else:
#     print("Adult but did you pass ur exam lol")

# temp = input("What is the temperature? ")

# if temp < 20:
#     print("Read indoors.")
# elif temp <= 30:
#     print("Go touch grass.")
# else:
#     print("Go touch water.")

grade = input("What is ur grade? ")
if grade == 100:
    print("Ranking is S tier")
elif grade > 89:
    print("Your ranking is A tier")
elif grade > 79:
    print("Your ranking is B tier")
elif grade > 69:
    print("Your tier is D tier")
elif grade < 60:
    print("Your ranking is tier is F")
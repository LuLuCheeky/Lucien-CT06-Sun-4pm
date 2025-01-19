print("Hello from lesson 2")

######## Write the pseudocode in comments for task 2 here
# Using comments, translate the code shown on screen into pseudocode.

######## Write the pseudocode in comments for task 3 here
# Using comments, translate the code shown on screen into pseudocode.

# Age = (11)
# print(Age)

# x = 10
# x = 20
# print(x)


# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
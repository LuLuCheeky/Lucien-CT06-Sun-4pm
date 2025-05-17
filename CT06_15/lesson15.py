# counter = 0
# def increment_counter():
#     global counter
#     counter += 1

# increment_counter()
# increment_counter()
# increment_counter()
# print(counter)  

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        print("False")

num = [
    3,
    8,
    23456,
    1243
]

for i in range(len(num)):
    isEven(num[i + 1])
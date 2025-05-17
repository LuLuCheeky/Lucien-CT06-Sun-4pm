# counter = 0
# def increment_counter():
#     global counter
#     counter += 1

# increment_counter()
# increment_counter()
# increment_counter()
# print(counter)  

# def isEven(n):
#     return n % 2 == 0

# numbers = [2345643, 2143564,1324565,112353]

# for n in numbers:
#     if isEven(n):
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")
def sumOfSquares(n2):
    def square(n):
        return n * n
num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(f"The square of {num} is {square(num)}")

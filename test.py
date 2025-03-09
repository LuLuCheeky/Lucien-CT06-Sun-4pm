# name = input("Whats your name? ")
# print("Nice to meet you," , name + "!")

Start = int(input("What number do you want to start at? "))
End = int(input("WHat number do you want to end at? "))
Increment = int(input("What do you want the increment to be? "))
Print = ""
for i in range(Start, End, Increment):
    Print = Print, i
print(Print)
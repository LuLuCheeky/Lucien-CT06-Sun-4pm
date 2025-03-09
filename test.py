name = input("Whats your name? ")
print("Nice to meet you," , name + "!")

Start = int(input("What number do you want to start at? "))
End = int(input("What number do you want to end at? "))
Increment = int(input("What number do you want the increment to be? "))
for i in range(Start, End + 1, Increment):
    
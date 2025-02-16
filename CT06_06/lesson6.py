# print("Hello from lesson 6")

numStu = int(input("How many students in the class are there? "))
totalMarks = 0
for i in numStu:
    #Average = the sum of ALL the numbers divided by num of numbers
    totalMarks = totalMarks + int(input("How much did student " + numStu - i + " get? " ))
print(totalMarks)
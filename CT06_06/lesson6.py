# print("Hello from lesson 6")

numStu = int(input("How many students in the class are there? "))
totalMarks = 0
stu = 1
for i in range(numStu):
    #Average = the sum of ALL the numbers divided by num of numbers
    totalMarks = totalMarks + int(input("How much did student number " + stu + " get? " ))
print("The average score of all the students were " + str(totalMarks / numStu))
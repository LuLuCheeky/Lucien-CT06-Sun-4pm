# # age = input('How old are you this year? ')
# # print('You were born in' ,  2025 - int(age) , '.')

# Name = input("Whats the participant's name? ")
# YearBorn = int(input("What year was the participant born in? "))
# Message = input("Give the participant a personalised massage: ")

# Age = 2025 - YearBorn

# Ending = 'th'

# if Age is 11 or 12 or 13:
#     Ending = 'th'
# if Age 

# print("Happy" + Age + "th brithday" + Name + "!" + Message )

# start = int(input('staring? '))
# stop = int(input('stopping? '))
    

# for i in range(start, stop + 1):
#     print(i)

# starting = int(input("Add until? "))

# total = 0

# for i in range(0, starting + 1):
#     num = num + i
# print(num)

num = 1
end = 3
spacingSymbol = ' '
tree = '*'
add = 2
howManyTree = 1
for i in range(num, end):
    spacing = end * end - num
    spacing = spacing / 2
    howManyTree2 = howManyTree * num
    print(spacingSymbol * spacing , tree * howManyTree2 , spacingSymbol * spacing)
    howManyTree = howManyTree + add

# # import turtle

# # window = turtle.Screen()
# # window.setup(width=600, height=400)
# #task1
# # t = turtle.Turtle()
# # t.forward(2)
# # t.speed(60)

# #task 2
# # import turtle

# # window = turtle.Screen()
# # window.setup(width=600, height=400)

# # t = turtle.Turtle()
# # for i in range(3):
# #     t.forward(100)
# #     t.left(360/3)
# # t.speed(60)

# #task 3
# import turtle

# window = turtle.Screen()
# window.setup(width=600, height=400)

# t = turtle.Turtle()
# for i in range(360):
#     t.forward(3)
#     t.left(1)
# for i in range(360):
#     t.forwad
# t.speed(60)



# ## Task 3: Drawing
# # Given the number of sides and each interior angle, draw each of the
# # following shapes using a loop and the following functions:
# #     .seth()
# #     .up()
# #     .down()
# #     .forward()
# #     .backward()
# #     .left()
# #     .right()

# # **Task 3a**: Draw a line
# # Number of sides: 1
# # Interior angle: NA
# import turtle
# window = turtle.Screen()
# window.setup(width = 1000, height = 1000)
# t = turtle.Turtle()
# t.seth(0)
# t.forward(200)


# window.mainloop()

# # **Task 3b**: Draw a triangle
# # Number of sides: 3
# # Interior angle: 120
# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# t = turtle.Turtle()
# for i in range(3):
#     t.left(360/3)
#     t.forward(100)


# window.mainloop()
# # **Task 3c**: Draw a square
# # Number of sides: 4
# # Interior angle: 90

# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# t = turtle.Turtle()
# for i in range(4):
#     t.left(360/4)
#     t.forward(50)

# window.mainloop()

# # **Task 3d**: Draw a pentagon
# # Number of sides: 5
# # Interior angle: 72

# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# t = turtle.Turtle()
# for i in range(5):
#     t.left(360/5)
#     t.forward(50)

# window.mainloop()

# # **Task 3e**: Draw a hexagon
# # Number of sides: 6
# # Interior angle: 60

# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# t = turtle.Turtle()
# for i in range(6):
#     t.left(360/6)
#     t.forward(50)

# window.mainloop()

# # **Task 3f**: Draw a circle
# # Number of sides: 360
# # Interior angle: 1
# window.mainloop()

# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# t = turtle.Turtle()
# for i in range(360):
#     t.left(360/360)
#     t.forward(1)

# window.mainloop()

# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# t = turtle.Turtle()
# for i in range(2):
#     t.penup
#     t.goto(0, 0)
#     t.pendown
#     t.forward(300)
#     t.left(180)
# t.left(90)
# for i in range(2):
#     t.penup
#     t.goto(0, 0)
#     t.pendown
#     t.forward(200)
#     t.left(180)



# window.mainloop()

# import random
# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)
# t = turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("green")
# t.hideturtle()
# for i in range(10):
#     x = random.randint(-300, 300)
#     y = random.randint(-200, 200)
#     t.penup()
#     t.goto(x, y)

#     for i in range(4):
#         t.pendown()
#         t.forward(30)
#         t.left(90)
    
#     t.penup()
#     t.sety(y - 40)
#     t.write(t.pos(), align="center")



# window.mainloop()



import random
import turtle
window = turtle.Screen()
window.setup(width = 400, height = 400)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("green")
t.hideturtle()
xLimit = 180
yLimit = 180
t.penup()
t.goto(-xLimit, -yLimit)
while True:
    while t.xcor() < xLimit:
        t.forward(1)
    t.left(90)
    while t.ycor() > yLimit:
        t.forward(1)
    t.left(90)
    while t.xcor() > -xLimit:
        t.forward(1)
    t.left(90)
    while t.ycor < -yLimit:
        t.forward(1)
    t.left(90)
    break


window.mainloop()
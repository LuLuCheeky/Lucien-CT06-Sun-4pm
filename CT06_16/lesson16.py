import turtle 


def setup_screen(screenWidth, screenHeight):
    window = turtle.Screen()
    window.setup(width=screenWidth, height=screenHeight)
    return window
def create_blue_ball():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    return ball
def move_ball(ball, dx, dy):
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)
dx = 2
dy = 2
setupW = 300
setupH = 500
window = setup_screen(setupW, setupH)
ball = create_blue_ball()
move_ball(ball, dx, dy)
window.mainloop()

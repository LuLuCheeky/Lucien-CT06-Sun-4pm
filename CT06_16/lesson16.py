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
def check_X(ball, screenWidth):
    if ball.xcor() > (screenWidth / 2) or ball.xcor() < (-screenWidth / 2):
        return True
def check_y(ball, screenHeight):
    if ball.ycor() > (screenHeight / 2) or ball.ycor() < (-screenHeight / 2):
        return True
dx = 2
dy = 2
setupW = 300
setupH = 500
window = setup_screen(setupW, setupH)
ball = create_blue_ball()
while True:
    move_ball(ball, dx, dy)
    if check_X(ball, setupW):
        dx *= -1
    if check_y(ball, setupH):
        dy *= -1
window.mainloop()

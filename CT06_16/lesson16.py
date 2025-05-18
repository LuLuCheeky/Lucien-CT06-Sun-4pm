import turtle 


def setup_screen(screenWidth, screenHeight):
    window = turtle.Screen()
    window.setup(width=screenWidth, height=screenHeight)
    return window

def create_blue_ball():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    return ball

setupW = 300
setupH = 500
window = setup_screen(setupW, setupH)
ball = create_blue_ball()


window.mainloop()

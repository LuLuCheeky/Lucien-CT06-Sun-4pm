import turtle 


def setup_screen(screenWidth, screenHeight):
    window = turtle.Screen()
    window.setup(width=screenWidth, height=screenHeight)
    return window

setupW = 300
setupH = 500
window = setup_screen(setupW, setupH)

window.mainloop()

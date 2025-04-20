import turtle

window = turtle.Screen()
window.setup(width=600, height=400)

t = turtle.Turtle()
t.shape("hexagon")
t.fillcolor("orange")
t.speed(60)

window.mainloop()
import turtle
from turtl import draw_diamond

window = turtle.Screen()
window.bgcolor("#D3D3D3")

fl = turtle.Turtle()
fl.shape("turtle")
fl.color("#800020")

for i in range(36):
    draw_diamond(fl, 50)
    fl.right(10)

fl.right(90)
fl.forward(200)
window.exitonclick()

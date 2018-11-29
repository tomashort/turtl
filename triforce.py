import turtle
from turtl import draw_triforce

window = turtle.Screen()
window.bgcolor("#D3D3D3")

fr = turtle.Turtle()
fr.shape("turtle")
fr.color("#800020")
fr.pencolor("#000080")

draw_triforce(fr, 200, 3)
window.exitonclick()

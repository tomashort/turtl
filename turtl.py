import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("#D3D3D3")
    
    sq = turtle.Turtle()
    sq.shape("turtle")
    sq.speed(1)
    sq.color("#800020")

    for i in range(4):
        sq.forward(100)
        sq.right(90)

    window.exitonclick()


draw_square()

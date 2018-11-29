import turtle

def draw_square(turtl, side_length=100):
    for i in range(4):
        turtl.forward(side_length)
        turtl.right(90)

def draw_circle(turtl, radius=100):
    turtl.circle(radius)

def draw_triangle(turtl, side_length=100):
    for i in range(3):
        turtl.forward(side_length)
        turtl.right(120)

def draw_diamond(turtl, side_length=100):
    turtl.forward(side_length)
    turtl.right(60)
    turtl.forward(side_length)
    turtl.right(120)
    turtl.forward(side_length)
    turtl.right(60)
    turtl.forward(side_length)
    turtl.right(120)

if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("#D3D3D3")
    
    sq = turtle.Turtle()
    sq.shape("turtle")
    sq.color("#800020")

    for i in range(36):
        draw_square(sq)
        sq.right(10)
        
    window.exitonclick()

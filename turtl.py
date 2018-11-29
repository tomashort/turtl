import turtle

def draw_square(turtl, side_length=100):
    for i in range(4):
        turtl.forward(side_length)
        turtl.right(90)

def draw_circle(turtl, radius=100):
    turtl.circle(radius)

def draw_triangle(turtl, side_length=100, fill=False):
    if fill == True:
        turtl.begin_fill()
    for i in range(3):
        turtl.forward(side_length)
        turtl.left(120)
    if fill == True:
        turtl.end_fill()

def draw_diamond(turtl, side_length=100):
    turtl.forward(side_length)
    turtl.right(60)
    turtl.forward(side_length)
    turtl.right(120)
    turtl.forward(side_length)
    turtl.right(60)
    turtl.forward(side_length)
    turtl.right(120)

def draw_triforce(turtl, side_length, levels):
    
    def triforce_recall():
        if levels > 1:
            draw_triforce(turtl, side_length / 2, levels - 1)

        if levels == 1:
            draw_triangle(turtl, side_length / 2, True)
        else:
            draw_triangle(turtl, side_length / 2)

    triforce_recall()
    turtl.forward(side_length / 2)
    triforce_recall()
    turtl.left(120)
    turtl.forward(side_length / 2)
    turtl.right(120)
    triforce_recall()
    turtl.right(120)
    turtl.forward(side_length / 2)
    turtl.left(120)

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

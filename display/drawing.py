import turtle

# Move without drawing
def move_to(t: turtle.RawTurtle, x: float, y: float):
    t.goto(x, y)
   
# Draw polygon
def draw_polygon(t: turtle.RawTurtle, sides: int, length: float, outline: str, fill: str, x: float, y: float):
    move_to(t, x, y)
    t.pendown()
    t.color(outline)
    t.fillcolor(fill)
    t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)
    t.end_fill()
    t.penup()


# Draw circle
def draw_circle(t: turtle.RawTurtle, radius: float, outline: str, fill: str, x: float, y: float):
    move_to(t, x, y)
    t.pendown()
    t.color(outline)
    t.fillcolor(fill)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()
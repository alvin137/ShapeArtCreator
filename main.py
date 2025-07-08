import turtle

# 🎉 Welcome and get user's name
print("🎨 Welcome to the Shape Art Creator!")
name = input("Please enter your name: ")
print(f"Hello, {name}! Let's start drawing shapes!")


#set up the turtle
t = turtle.Turtle()
t.speed(2)


# Move without drawing
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
   
# Draw polygon
def draw_polygon(sides, length, outline, fill, x, y):
    move_to(x, y)
    t.color(outline)
    t.fillcolor(fill)
    t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)
    t.end_fill()


# Draw circle
def draw_circle(radius, outline, fill, x, y):
    move_to(x, y)
    t.color(outline)
    t.fillcolor(fill)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
   
#main loop
while True:
    print("\nWhich shape do you want to draw?")#\n means a newline (a blank line before the text).
    print("1. Triangle")
    print("2. Square")
    print("3. Circle")
    print("4. Hexagon")
    choice = input("Your choice: ")

    if choice == '1':
        sides = 3
    elif choice == '2':
        sides = 4
    elif choice == '3':
        sides = 0  # circle special case
    elif choice == '4':
        sides = 6
    else:
        print("Invalid choice.")
        continue

    outline = input("Enter outline color: ")
    fill = input("Enter fill color: ")
    x = int(input("Enter X position: "))
    y = int(input("Enter Y position: "))

    if sides == 0:
        radius = int(input("Enter radius: "))
        draw_circle(radius, outline, fill, x, y)
    else:
        length = int(input("Enter side length: "))
        draw_polygon(sides, length, outline, fill, x, y)

    again = input("Draw another? (yes/no): ").lower()
    if again != "yes":
        break

print(f"\nThank you for using Shape Art Creator, {name}! Goodbye 👋")
t.hideturtle()
turtle.done()
## preparing
def clear(canvas):
    canvas.delete("all")
    #screen.clear()

def show_speech(canvas, text, x, y, length):
    bubble = canvas.create_rectangle(x-10, y-30, x+length, y, fill="white", outline="black", width=2)
    label = canvas.create_text(x+5, y-15, text=text, anchor="w", font=("Arial", 14, "bold"))
    return bubble, label
    
def float_dog(canvas, root, dog_id, step=0):
    if canvas.coords(dog_id):  
        dy = 1 if step % 20 < 10 else -1
        canvas.move(dog_id, 0, dy)
        root.after(10, lambda: float_dog(canvas, root, dog_id, step + 1))

def float_title(canvas, root, title_id, step=0):
    if canvas.coords(title_id):  
        dy = 1.5 if step % 20 < 10 else -1.5
        canvas.move(title_id, 0, dy)
        root.after(100, lambda: float_title(canvas, root, title_id, step + 1))

##  main function
def show_title(canvas, root):
    title_id = canvas.create_text(
        0, 0,
        text="Shape Art Creator",
        font=("Helvetica", 30, "bold"),
        fill="black"
    )
    float_title(canvas, root, title_id)
    return title_id

def ask_name(canvas, root, dog_img):
    dog_id = canvas.create_image(-100, 0, image=dog_img, anchor="center")
    show_speech(canvas, "What's your name?", -40, -50, 200)
    float_dog(canvas, root, dog_id)

def dance(canvas, root, dog_img, step=0):
    if step == 0:
        dog_id = canvas.create_image(-100, 0, image=dog_img, anchor="center")
        dance.dog_id = dog_id
    if step >= 100:
        return
    dx = 15 if step % 2 == 0 else -15
    dy_cycle = step % 8
    if dy_cycle in [0, 4]:
        dy = -20
    elif dy_cycle in [2, 6]:
        dy = 20
    else:
        dy = 0
    canvas.move(dance.dog_id, dx, dy)
    root.after(20, lambda: dance(canvas, root, dog_img, step + 1))
    
def ask_again(canvas, root, dog_img):
    dog_id = canvas.create_image(-100, 0, image=dog_img, anchor="center")
    show_speech(canvas, "Draw another?", -40, -50, 200)
    float_dog(canvas, root, dog_id)

def say_goodbye(canvas, root, dog_img):
    dog_id = canvas.create_image(-100, 0, image=dog_img, anchor="center")
    show_speech(canvas, "Thank you!", -40, -50, 150)
    float_dog(canvas, root, dog_id)

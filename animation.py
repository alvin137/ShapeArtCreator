from tkinter import Canvas, Tk, PhotoImage

class AnimationHandler:
    def __init__(self, canvas: Canvas, root: Tk, dog_img: PhotoImage):
        self.canvas = canvas
        self.root = root
        self.dog_img = dog_img
        self.elements: list[int] = []

    ## preparing
    def clear(self):
        for e in self.elements:
            self.canvas.delete(e)

    def show_speech(self, text: str, x: float, y: float, length: float):
        bubble = self.canvas.create_rectangle(x-10, y-30, x+length, y, fill="white", outline="black", width=2)
        label = self.canvas.create_text(x+5, y-15, text=text, anchor="w", font=("Arial", 14, "bold"))
        return bubble, label
    
    def float_dog(self, dog_id: int, step: int=0):
        if self.canvas.coords(dog_id):  
            dy = 1 if step % 20 < 10 else -1
            self.canvas.move(dog_id, 0, dy)
            self.root.after(50, lambda: self.float_dog(dog_id, step + 1))

    def float_title(self, title_id: int, step: int=0):
        if self.canvas.coords(title_id):  
            dy = 1.5 if step % 20 < 10 else -1.5
            self.canvas.move(title_id, 0, dy)
            self.root.after(100, lambda: self.float_title(title_id, step + 1))

    def float_subtitle(self, subtitle_id: int, step: int=0):
        if self.canvas.coords(subtitle_id):  
            dy = 1.5 if step % 20 < 10 else -1.5
            self.canvas.move(subtitle_id, 0, dy)
            self.root.after(100, lambda: self.float_subtitle(subtitle_id, step + 1))

    def create_dog(self):
        dog_id = self.canvas.create_image(-100, 0, image=self.dog_img, anchor="center")
        self.elements.append(dog_id)
        return dog_id

    ##  main function
    def show_title(self):
        title_id = self.canvas.create_text(
            0, -5,
            text="Shape Art Creator",
            font=("Helvetica", 35, "bold"),
            fill="black",
            justify="center"
        )
        self.float_title(title_id)
        self.elements.append(title_id)
        subtitle_id = self.canvas.create_text(
            0, 50,
            text="Click to Start",
            font=("Helvetica", 20, "bold"),
            fill="black",
            justify="center"
        )
        self.float_subtitle(subtitle_id)
        self.elements.append(subtitle_id)

    def ask_name(self):
        dog_id = self.create_dog()
        self.elements += self.show_speech("What's your name?", -40, -50, 200)
        self.float_dog(dog_id)

    def dance(self, step: int = 0):
        if step == 0:
            dog_id = self.create_dog()
            self.dog_id = dog_id
        if step >= 19:
            return
        dx = 15 if step % 2 == 0 else -15
        dy_cycle = step % 8
        if dy_cycle in [0, 4]:
            dy = -20
        elif dy_cycle in [2, 6]:
            dy = 20
        else:
            dy = 0
        self.canvas.move(self.dog_id, dx, dy)
        self.root.after(100, lambda: self.dance(step + 1))
        
    def ask_again(self):
        dog_id = self.create_dog()
        bubble_id, label_id = self.show_speech("Nice shape!!", -40, -50, 200)
        self.elements += [bubble_id, label_id]
        self.speech_label_id = label_id
        self.float_dog(dog_id)
        self.root.after(2000, lambda: self.canvas.itemconfig(self.speech_label_id, text="Draw another?"))
    
    def ask_color(self):
        dog_id = self.create_dog()
        self.elements += self.show_speech("Please select color", -40, -50, 200)
        self.float_dog(dog_id)

    def say_goodbye(self):
        dog_id = self.create_dog()
        self.elements += self.show_speech("Thank you!", -40, -50, 150)
        self.float_dog(dog_id)

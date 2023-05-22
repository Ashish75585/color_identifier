from color_identifier import ColorIdentifier
import tkinter as t
from PIL import ImageTk, Image

class ChooseImage(ColorIdentifier):
    def __init__(self, img_path):
        super().__init__()
        self.img_path = img_path

    def call_identify_color(self):
        self.identify_color(self.img_path)


    def second_window(self):
        global img
        top = t.Toplevel()
        top.config(padx=20, pady=20)
        image = Image.open(self.img_path)
        img = ImageTk.PhotoImage(image)
        label = t.Label(top, image=img)
        label.config(padx=20, pady=50)
        label.grid(row=0, column=0)
        generate_button = t.Button(top, text="Generate Colors", command=self.call_identify_color, width=30, bg="blue", foreground="white", font=("Arial", 15, "italic"))
        generate_button.grid(row=1, column=0)



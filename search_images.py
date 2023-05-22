import requests

import tkinter as t

from choose_image import ChooseImage
from PIL import ImageTk, Image
from tkinter import messagebox


class SearchImages(ChooseImage):
    def __init__(self):
        super().__init__("image.jpeg")
        self.keyword = ""
        self.size = "400x400"

    def search(self):
        global img, entry
        root = t.Toplevel(width=400, height=400)
        root.config(padx=20, pady=20)
        root.title("Search Online")
        icon = Image.open("search_icon.png")
        img = ImageTk.PhotoImage(icon)
        label1 = t.Label(root, image=img)
        label1.place(x=85, y=0)

        label2 = t.Label(root, text="Enter Object's Name:", font=("Arial", 13, "normal"))
        label2.place(x=0, y=220)

        entry = t.Entry(root, width=25, font=("Arial", 13, "normal"))
        entry.place(x=0, y=250)
        entry.focus()
        self.keyword = entry.get()
        print(self.keyword)

        button = t.Button(root, text="Search", font=("Arial", 13, "normal"), width=10, bg="green", foreground="white", command=self.call_second_window_for_entered_name_search)
        button.place(x=240, y=245)

        label3 = t.Label(root, text="------------------OR------------------", font=("Arial", 15, "italic"))
        label3.place(x=27, y=280)

        button1 = t.Button(root, text="Search Random Image", font=("Arial", 13, "normal"), width=35, bg="orange", foreground="white", command=self.call_second_window_for_random_search)
        button1.place(x=10, y=315)



    def call_second_window_for_entered_name_search(self):
        self.keyword = entry.get()

        if len(self.keyword) == 0:
            messagebox.showwarning(title="Empty Field", message="Please enter the text into Entry field")

        else:
            entry.delete(0, t.END)
            self.image_from_internet()
            self.second_window()

    def call_second_window_for_random_search(self):
        self.keyword = "random"
        self.image_from_internet()
        self.second_window()



# **************************** Searching Image from internet ***********************************
    def image_from_internet(self):
        # try:
        #     # this block will execute if we run the code from the terminal and pass image name.
        #     self.keyword = sys.argv[1]
        #     print(self.keyword)
        # except:
        #     # this block will run if we don't pass any image name.
        #     self.keyword = "random"
        #
        # try:
        #     # this block will execute if we run the code from the terminal and pass iamge size.
        #     self.size = sys.argv[2]
        #     print(self.size)
        # except:
        #     # this block will run if we don't pass any image size.
        #     self.size = "400x400"

        # messagebox.showwarning(title="Empty Field", message="Please enter text into field.")

        # else:
        # print(self.keyword)
        r = requests.get(f"https://source.unsplash.com/{self.size}/?{self.keyword}")

        with open("./image.jpeg", "wb") as f:  # "wb" means image will be open in the form of binary format.
            f.write(r.content)

# **************************** Searching Image from internet ***********************************




from color_identifier import ColorIdentifier
import tkinter as t
from tkinter import filedialog
from choose_image import ChooseImage
from search_images import SearchImages
from tkinter import messagebox


# creating class of class SearchImage
s_image = SearchImages()


# Creating object of class ColorIdentifier.
c = ColorIdentifier()



# def img_from_web():
#     s_image.image_from_internet()
#     c2 = ChooseImage("image.jpeg")
#     c2.second_window()

def img_from_folder():
    try:
        filename = filedialog.askopenfilename(initialdir=r"C:\Users\DELL\Pictures\Saved Pictures", title="Select an Image",
                                              filetypes=(("all files", "*.*"),))
        if len(filename) != 0:
            c2 = ChooseImage(filename)
            c2.second_window()
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="File Not Found")


# function to call the search method of class SearchImage.
def call_search():
    call = s_image.search()


# ******************************* Creating GUI***************************************

window = t.Tk()
window.geometry("300x300")
window.title("Image Color Identifier")

window.config(padx=30, pady=30)

img_png = t.PhotoImage(file="color2.png")
canvas = t.Canvas(width=160, height=160)
canvas.create_image(80, 80, image=img_png)
canvas.place(x=40, y=0)


button1 = t.Button(text="Pick image from Folder", width=25, command=img_from_folder)
button1.place(x=35, y=190)

button2 = t.Button(text="Pick image from Web", width=25, command=call_search) # img_from_web  # call_search
button2.place(x=35, y=230)

window.mainloop()



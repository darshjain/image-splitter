import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import filedialog

rows = columns = 3

# ------------------ Window---------------------
window = tk.Tk()
window.geometry("700x700")
window.grid_columnconfigure((0, 1), weight=1)
window.title("Image Splitter")

#------------------Blank PlaceHolder------------
blank_image=Image.open("blank.png")
blank_image=blank_image.resize((500,500),Image.ANTIALIAS)
blank_image = ImageTk.PhotoImage(blank_image)
# label_display["image"]=blank_image

#------------------Functions--------------------
def add_photo_dialog():
    global photo_selected
    filename = filedialog.askopenfilename()

    image = Image.open(filename)
    image = image.resize((500, 500), Image.ANTIALIAS)
    photo_selected = ImageTk.PhotoImage(image)
    label_display["image"] = photo_selected

# ------------------Components---------------------
add_file = tk.Button(
    text="ADD FILE",
    width=70,
    height=3,
    command=add_photo_dialog,
    font=('Helvetica', 10, 'bold'),
)
label_display = tk.Label(
    text="",
    image=blank_image,
    width=500,
    height=500,
)
label_display.grid(column=0, row=0)
add_file.grid(column=0, row=1)
window.mainloop()

import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import filedialog

rows = columns = 3


def add_photo_dialog():
    global photo_selected
    filename = filedialog.askopenfilename()
    
    image=Image.open(filename)
    image = image.resize((450, 350), Image.ANTIALIAS)
    photo_selected = ImageTk.PhotoImage(image)
    label_display["image"]=photo_selected


# ------------------ window---------------------
window = tk.Tk()
window.geometry("700x700")
window.grid_columnconfigure((0, 1), weight=1)
window.title("Image Splitter")

# ------------------buttons---------------------
add_file = tk.Button(
    text="ADD FILE",
    width=70,
    height=3,
    command=add_photo_dialog,
    font=('Helvetica', 10, 'bold'),
)
label_display = tk.Label(
    text="",
    image="",
    width=500,
    height=500,
    border=4,
)

add_file.grid(column=0, row=0)
label_display.grid(column=0, row=2)
window.mainloop()

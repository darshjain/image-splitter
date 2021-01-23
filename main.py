import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import filedialog

global rows, columns
rows = columns = 3

# ------------------ Window---------------------
window = tk.Tk()
window.geometry("900x700")
window.grid_columnconfigure((0, 1), weight=1)
window.title("Image Splitter")

# ------------------Blank PlaceHolder------------
blank_image = Image.open("blank.png")
blank_image = blank_image.resize((800, 500), Image.ANTIALIAS)
blank_image = ImageTk.PhotoImage(blank_image)

# ------------------Functions--------------------

def add_photo_dialog():
    global photo_selected
    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    image = image.resize((800, 500), Image.ANTIALIAS)
    photo_selected = ImageTk.PhotoImage(image)
    label_display["image"] = photo_selected

def divide_photo():
    rows=int(rows_textbox.get())
    columns=int(columns_textbox.get())
    width_image=int(800/rows)
    height_image=int(500/columns)

    filename = filedialog.askopenfilename()
    image = Image.open(filename)
    w,h=image.size()

    # cropped_images={}
    # for i in range(rows-1):
    #     for j in range(columns-1):
    #         box=(i*width_image,j*height_image,(i+1)*height_image,(j+1)*height_image)
    #         cropped_images=(photo_selected.crop(box))

# ------------------Components---------------------
add_file = tk.Button(
    text="ADD FILE",
    width=70,
    height=3,
    command=add_photo_dialog,
    font=('Helvetica', 10, 'bold'),
)
process_photo = tk.Button(
    text="Process And Save",
    width=70,
    height=3,
    command=divide_photo,
    font=('Helvetica', 10, 'bold'),
)
label_display = tk.Label(
    text="",
    image=blank_image,
    width=800,
    height=500,
)
label_rows = tk.Label(
    text="Number Of Rows to be divided",
    height=1,
    width=30,
)
label_columns = tk.Label(
    text="Number Of Columns to be divided",
    height=1,
    width=30,
)
rows_textbox = tk.Entry(
    width=5,
    borderwidth=5,
)
columns_textbox = tk.Entry(
    width=5,
    borderwidth=5,
)
# --------------------Add to Layout-------------------
label_display.grid(column=0, row=0, columnspan=4)
add_file.grid(column=0, row=3, columnspan=2)
process_photo.grid(column=2, row=3, columnspan=2)
label_columns.grid(column=0, row=2)
columns_textbox.grid(column=1, row=2)
label_rows.grid(column=2, row=2)
rows_textbox.grid(column=3, row=2)


window.mainloop()

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
    global filename
    filename = filedialog.askopenfilename()

    image = Image.open(filename)
    image = image.resize((800, 500), Image.ANTIALIAS)
    photo_selected = ImageTk.PhotoImage(image)
    label_display["image"] = photo_selected

def image_crop(input, xPieces, yPieces):
    filename, file_extension = os.path.splitext(input)
    im = Image.open(input)
    imgwidth, imgheight = im.size
    height = imgheight // yPieces
    width = imgwidth // xPieces
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
            try:
                a.save("images/" + filename + "-" + str(i) + "-" + str(j) + file_extension)
            except:
                pass

def divide_photo():
    rows=int(rows_textbox.get())
    columns=int(columns_textbox.get())
    image_crop(filename,rows,columns)
    # image = Image.open(filename)
    # width,height=image.size
    # width_image=int(800/rows)
    # height_image=int(500/columns)

    # grid = list(product(range(0, height-height%height_image, height_image), range(0, width-width%width_image, width_image)))

    # for i,j in grid:
    #     box = (j, i, j+rows, i+columns)

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

import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import filedialog,messagebox

global rows, columns
rows = columns = 3

# ------------------ Window---------------------
window = tk.Tk()
window.geometry("900x700")
window.grid_columnconfigure((0, 1), weight=1)
window.title("Image Splitter")

# ---------------Blank PlaceHolder---------------
blank_image = Image.open("Assets/blank.png")
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


def image_crop(input, x_pieces, y_pieces):
    try:
        filename, file_extension = os.path.splitext(input)
        image_handle = Image.open(input)
        image_width, image_height = image_handle.size
        height = image_height // y_pieces
        width = image_width // x_pieces
        for i in range(0, y_pieces):
            for j in range(0, x_pieces):
                box = (j * width, i * height, (j + 1)
                       * width, (i + 1) * height)
                out = os.path.join("Output//", f'{i}_{j}{file_extension}')
                image_handle.crop(box).save(out)

        tk.messagebox.showinfo(
            title="Successful", message="Images saved in Output folder")
    except:
        tk.messagebox.showinfo(
            title="Error", message="Error While Generating images")


def divide_photo():
    try:
        rows = int(rows_textbox.get())
        columns = int(columns_textbox.get())
        image_crop(filename, rows, columns)
    except:
        tk.messagebox.showinfo(
            title="Error", message="Please Enter Values of rows and columns")


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
    width=71,
    height=3,
    command=divide_photo,
    font=('Roman', 10, 'bold'),
)
label_display = tk.Label(
    text="",
    image=blank_image,
    width=801,
    height=501,
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
label_preview = tk.Label(
    text="Preview",
    font=('Helvetica', 10, 'bold'),
)
# --------------------Add to Layout-------------------
label_display.grid(column=0, row=0, columnspan=4)
add_file.grid(column=0, row=3, columnspan=2)
process_photo.grid(column=2, row=3, columnspan=2)
label_columns.grid(column=0, row=2)
columns_textbox.grid(column=1, row=2)
label_rows.grid(column=2, row=2)
rows_textbox.grid(column=3, row=2)
label_preview.place(x=60, y=10)

window.mainloop()

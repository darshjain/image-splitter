import tkinter as tk
import os
from PIL import Image
from tkinter import filedialog

rows = columns = 3

def add_photo_dialog():
    global photo
    filename = filedialog.askopenfilename()
    photo = tk.PhotoImage(file=filename)
    update_photo()
def update_photo():
    label_display["image"]=photo

#------------------ window---------------------
window = tk.Tk()
window.geometry("700x700")
window.grid_columnconfigure((0, 1), weight=1)
window.title("Image Splitter")

#------------------buttons---------------------
add_file = tk.Button(
    text="ADD FILE",
    width=70,
    height=3,
    command=add_photo_dialog,
    font=('Helvetica', 10, 'bold'),
)
label_display=tk.Label(
    text="",
    image="",
    width=500,
    height=500,
    border=4,
)

add_file.grid(column=0,row=0)
label_display.grid(column=0,row=2)
window.mainloop()

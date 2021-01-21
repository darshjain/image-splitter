import tkinter as tk
import os
from PIL import Image
from tkinter import filedialog

rows = columns = 3

def add_photo_dialog():
    global photo
    filename = filedialog.askopenfilename()
    photo = tk.PhotoImage(file=filename)

# window
window = tk.Tk()
window.geometry("500x500")
window.grid_columnconfigure((0, 1), weight=1)
window.title("Image Splitter")

# buttons
add_file = tk.Button(
    text="ADD FILE",
    width=70,
    height=3,
    command=add_photo_dialog,
    font=('Helvetica', 10, 'bold'),
)
add_file.grid(column=0,row=0)

window.mainloop()

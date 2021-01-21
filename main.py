import tkinter as tk
import os
from PIL import Image

rows = columns = 0


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
    # command=generate1,
    font=('Helvetica', 10, 'bold'),
)
add_file.grid(column=0,row=0)

window.mainloop()

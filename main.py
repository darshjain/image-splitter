import tkinter as tk
import os
from PIL import Image

rows=columns=0


#window
window=tk.Tk()
window.geometry("500x500")
window.grid_columnconfigure((0,1), weight=1)

window.title("Image Splitter")
window.mainloop()
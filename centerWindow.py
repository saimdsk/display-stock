import tkinter
import os

def center(loadApplication):
    loadApplication.update_idletasks()
    width = loadApplication.winfo_width()
    height = loadApplication.winfo_height()
    x = (loadApplication.winfo_screenwidth() // 2) - (width // 2)
    y = (loadApplication.winfo_screenheight() // 2) - (height // 2)
    loadApplication.geometry('{}x{}+{}+{}'.format(width, height, x, y))

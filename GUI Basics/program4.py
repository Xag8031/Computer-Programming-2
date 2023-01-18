"""Contains only code to display the attached picture in the GUI window.
"""
from tkinter import Tk, Label
from PIL import ImageTk, Image 

root = Tk()
image = Image.open("wizard.jpg")
image = ImageTk.PhotoImage(image)
label = Label(root, image=image)
label.pack()
root.mainloop()

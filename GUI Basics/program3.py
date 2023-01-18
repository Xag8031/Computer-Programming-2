"""Contains only code to display the text "I am text" in the GUI window.
"""
from tkinter import Label, Tk

root = Tk()
label = Label(root, text="I am text")
label.grid(row=0, column=0)
root.mainloop()

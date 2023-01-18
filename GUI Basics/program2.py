"""Contains only code to display an input box in the GUI window.
"""
from tkinter import Entry, Tk

root = Tk()
entry = Entry(root)
entry.grid(row=0, column=0)
root.mainloop()

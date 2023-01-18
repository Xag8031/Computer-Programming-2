from tkinter import *
root = Tk()

#create a button
button = Button(root, text = "Push me!", command = lambda: print("pushed"))
button.pack()
root.mainloop()
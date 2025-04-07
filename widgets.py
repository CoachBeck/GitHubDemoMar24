from tkinter import *
from tkinter import ttk
root = Tk()
btn1 = ttk.Button(root)
btn1.config(text="Click!")
btn1.grid() #configure the geometry manager on its own line after
#the button has been created
root.mainloop()
from tkinter import *
import tkinter as tk
import sys
import time
 
def get_time(arg, canvas, var):
    myTime = time.localtime()
    currentTime = time.strftime("%I:%M:%S %p",myTime)
    canvas.itemconfig(var, text=currentTime)
    arg.after(1000, lambda: get_time(arg, canvas, var))
 
root = tk.Tk()
root.attributes('-fullscreen', True)
root.geometry("800x480")
img = PhotoImage(file='clockBackground.png')

canvas = tk.Canvas(root, width=800, height=480)
canvas.create_image(0,0, image = img, anchor = "nw")
currentTime = time.strftime("%I:%M:%S %p")
var = canvas.create_text(400, 240, text = get_time, fill="white", font = ("times", 60))

canvas.pack()
 
root.after(200, lambda: get_time(root, canvas, var))
root.mainloop()

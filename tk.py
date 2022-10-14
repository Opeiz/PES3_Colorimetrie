from email.mime import image
import sys
from cgi import test
from tkinter import *
from turtle import left
from PIL import ImageTk, Image
import cv2 

main = Tk()
main.geometry("960x540")
main.title('Visionneuse Numérique')
Label(main,text="Prévisualisation", font=('bold',12)).pack()

# How to return to images
pos = 34
path = "frames/frame" + str(pos) + ".jpg"
frame = Image.open(path)
frame = frame.resize((760,340))
last = ImageTk.PhotoImage(frame)

def Forward():  
    global pos
    pos = pos + 1
    try:
        img_label.config(image = last)
    except:  
        pos = -1  
        Forward()

def Backward():  
    global pos
    global img_label
    pos = pos - 1
    try:
        img_label.config(image = last)
    except:  
        pos = 0  
        Backward()


Frames = Frame(main,width=960,height=540,bg='white')
Frames.pack()

img_label = Label(Frames, image = last)
img_label.pack()

Button(main, text = 'Back', command = Backward, bg= 'light blue').place(x = 240, y = 50)  
Button(main, text = 'Next', command = Forward, bg = 'light blue').place(x = 540, y = 50)  

main.mainloop()
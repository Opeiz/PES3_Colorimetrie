from email.mime import image
import sys
from cgi import test
from tkinter import *
from turtle import left
from PIL import ImageTk, Image
import cv2
import os

# Some global parametres
pathFrames = "frames/"
allFrames = []
start = 0

numberFrames = len([entry for entry in os.listdir(pathFrames) if os.path.isfile(os.path.join(pathFrames, entry))])

main = Tk()
main.geometry("960x540")
main.title('Visionneuse Numérique')
Label(main,text="Prévisualisation", font=('bold',12)).pack()

# How to return to images
def ListImages(numberFrames):
    print("Starts procesing images")
    for i in list(range(numberFrames)):
        path = "frames/frame" + str(i) + ".jpg"
        frame = Image.open(path)
        frame = frame.resize((760,340))
        last = ImageTk.PhotoImage(frame)
        allFrames.append(last)
    print("Finish procesing images")
ListImages(numberFrames)

def Forward(start):
 
    global label
    global button_forward
    global button_back

    label = Label(image = allFrames[start-1])

    button_forward = Button(main, text="forward", command=lambda: Forward(start+1))
    button_back = Button(main, text="Back", command=lambda: Backward(start-1))

    print(start)
    if start == numberFrames-1:
        button_forward = Button(main, text="Forward", state=DISABLED)

def Backward(start):

    global label
    global button_forward
    global button_back
 
    label = Label(image = allFrames[start - 1])

    button_forward = Button(main, text="forward",command= lambda: Forward(start + 1))
    button_back = Button(main, text="Back",command= lambda: Backward(start - 1))

    print(start)
    if start == start:
        button_back = Button(main, Text="Back", state=DISABLED)
 


Frames = Frame(main,width=960,height=540,bg='white')
Frames.pack()

# img_label = Label(Frames, image = last)
label = Label(image=allFrames[start])
label.pack()

button_forward = Button(main, text = 'Next', command = lambda:Forward(start), bg = 'light blue').place(x = 540, y = 50)  
button_back = Button(main, text = 'Back', command = lambda:Backward(start), bg= 'light blue').place(x = 240, y = 50)  

main.mainloop()
from tkinter import *
import cv2
import numpy as np

w,h = 640,480

def callimage(num):

    path = "colors/frame" + str(num) + ".jpg"
    frame = cv2.imread(path)
    frame = cv2.resize(frame,(int(frame.shape[1]*0.4),int(frame.shape[0]*0.4)))

    cv2.imshow("Visionneuse",frame) 
    return frame

def forward(img_no):

    global button_forward
    global button_back
    global number
    number = img_no

    refresh(img_no)

    button_for = Button(root, text="Forward", command= lambda: forward(img_no+1))
    button_back = Button(root, text="Back", command= lambda: back(img_no-1))
    
    button_back.grid(row=3, column=0)
    button_for.grid(row=3, column=2)

def back(img_no):

    global button_forward
    global button_back
    global number
    number = img_no

    refresh(img_no)

    button_for = Button(root, text="Forward", command=lambda: forward(img_no+1))
    button_back = Button(root, text="Back", command=lambda: back(img_no-1))

    button_back.grid(row=3, column=0)
    button_for.grid(row=3, column=2)

def show_values():
    return (SliderR.get(), SliderG.get(), SliderB.get())

def refresh(num):

    ValueR, ValueG, ValueB = show_values()

    frame = callimage(num)
    
    frame = frame.astype("int64") + np.array([ValueB,ValueG,ValueR],dtype="int64")
    frame[frame>255] = 255
    frame[frame<0] = 0
    frame = frame.astype("uint8")
        
    cv2.imshow("Visionneuse",frame) 
    
def reset_Slider():
    SliderB.set(0)
    SliderG.set(0)
    SliderR.set(0)

root =Tk()

root.title("Visionneuse Numérique")

root.resizable(0,0)

# First Image to display
number = 0
callimage(number)

# Buttons
button_back = Button(root, text="Back",command=back, state= DISABLED).grid(row=3, column=0,padx=30,pady=8)  
button_forward = Button(root, text="Forward", command=lambda: forward(number+1)).grid(row=3, column=2)
button_refesh = Button(root, text="Refresh", command=lambda: refresh(number)).grid(row=3, column=1)
button_exit = Button(root, text="Exit", command=root.quit).grid(row=4, column=1,padx=30,pady=8)

red_label = Label(root, text="Red").grid(row=0, column=0)
SliderR = Scale(root, from_=-255 , to=255, orient=HORIZONTAL, length=300)
SliderR.grid(row=0, column=1, columnspan=2)

green_label = Label(root, text="Green").grid(row=1, column=0)
SliderG = Scale(root, from_=-255 , to=255, orient=HORIZONTAL, length=300)
SliderG.grid(row=1, column=1, columnspan=2)

blue_label = Label(root, text="Blue").grid(row=2, column=0)
SliderB = Scale(root, from_=-255 , to=255, orient=HORIZONTAL, length=300)
SliderB.grid(row=2, column=1, columnspan=2)

button_reset = Button(root, text="Reset", command=lambda: reset_Slider()).grid(row=4, column=0,padx=30,pady=8)

root.mainloop()
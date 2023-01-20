from tkinter import *
import customtkinter as ct
import cv2
import numpy as np


def callimage(num):

    path = "frames/frame" + str(num) + ".jpg" # Change frames to colors and viceversa, for RGB and BW tests
    frame = cv2.imread(path)
    value = 0.3 # Value for the size of the output frame
    frame = cv2.resize(frame,(int(frame.shape[1]*value),int(frame.shape[0]*value))) 

    cv2.imshow("Visionneuse",frame) 
    return frame

def forward(img_no):

    global button_forward
    global button_back
    global number
    number = img_no

    refresh(img_no)

    button_for = ct.CTkButton(master=root, text="Forward", command= lambda: forward(img_no+1))
    button_back = ct.CTkButton(master=root, text="Back", command= lambda: back(img_no-1))
    
    button_back.grid(row=3, column=0)
    button_for.grid(row=3, column=2)

def back(img_no):

    global button_forward
    global button_back
    global number
    number = img_no

    refresh(img_no)

    button_for = ct.CTkButton(master=root, text="Forward", command=lambda: forward(img_no+1))
    button_back = ct.CTkButton(master=root, text="Back", command=lambda: back(img_no-1))

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

root =ct.CTk()

root.title("Visionneuse Numérique")

root.resizable(0,0)

# First Image to display
number = 0
callimage(number)

# Buttons
button_back =       ct.CTkButton(master=root, text="Back",command=back, state= DISABLED).grid(row=3, column=0,padx=30,pady=8)  
button_forward =    ct.CTkButton(master=root, text="Forward", command=lambda: forward(number+1)).grid(row=3, column=2,padx=30,pady=8)
button_refesh =     ct.CTkButton(master=root, text="Refresh", command=lambda: refresh(number)).grid(row=3, column=1,padx=30,pady=8)
button_exit =       ct.CTkButton(master=root, text="Exit", command=root.quit).grid(row=4, column=1,padx=30,pady=8)

red_label =         ct.CTkLabel(master=root, text="Red").grid(row=0, column=0)
SliderR =           ct.CTkSlider(master=root, from_=-120 , to=120, hover=True)
SliderR.grid(row=0, column=1, columnspan=2)

green_label =       ct.CTkLabel(master=root, text="Green").grid(row=1, column=0)
SliderG =           ct.CTkSlider(master=root, from_=-120 , to=120)
SliderG.grid(row=1, column=1, columnspan=2)

blue_label =        ct.CTkLabel(master=root, text="Blue").grid(row=2, column=0)
SliderB =           ct.CTkSlider(master=root, from_=-120 , to=120)
SliderB.grid(row=2, column=1, columnspan=2)

button_reset =      ct.CTkButton(master=root, text="Reset", command=lambda: reset_Slider()).grid(row=4, column=0,padx=30,pady=8)

root.mainloop()
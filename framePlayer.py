from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk
import threading
import customtkinter as ct

w,h = 640,480

def callimage(num):

    path = "colors/frame" + str(num) + ".jpg"
    frame = cv2.imread(path)
    frame = cv2.resize(frame,(int(frame.shape[1]*0.4),int(frame.shape[0]*0.4)))

    #cv2.imshow("Visionneuse",frame) 
    return frame

# First Image to display
number = 0
ex_img = callimage(number)

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
    global ex_img
    global im
    global imgtk
    global imageViewed
    ValueR, ValueG, ValueB = show_values()

    frame = callimage(num)
    
    frame = frame.astype("int64") + np.array([ValueB,ValueG,ValueR],dtype="int64")
    frame[frame>255] = 255
    frame[frame<0] = 0
    frame = frame.astype("uint8")
        
    #cv2.imshow("Visionneuse",frame)
    ex_img = frame
    im = Image.fromarray(ex_img)
    imgtk = ImageTk.PhotoImage(image=im)
    imageViewed = Label(root, image=imgtk).grid(row=0, column=3, rowspan=4, columnspan=4, padx=10, pady=5)
    
def reset_Slider():
    SliderB.set(0)
    SliderG.set(0)
    SliderR.set(0)

root = ct.CTk()

root.title("Visionneuse Numérique")

root.resizable(0,0)



# Buttons
button_back = ct.CTkButton(master=root, text="Back",command=back, state= DISABLED).grid(row=3, column=0,padx=30,pady=8)  
button_forward = ct.CTkButton(master=root, text="Forward", command=lambda: forward(number+1)).grid(row=3, column=2,padx=30,pady=8)
button_refesh = ct.CTkButton(master=root, text="Refresh", command=lambda: refresh(number)).grid(row=3, column=1,padx=30,pady=8)
button_exit = ct.CTkButton(master=root, text="Exit", command=root.quit).grid(row=4, column=1,padx=30,pady=8)

red_label = ct.CTkLabel(master=root, text="Red").grid(row=0, column=0)
SliderR = ct.CTkSlider(master=root, from_=-255 , to=255, hover=True)
SliderR.grid(row=0, column=1, columnspan=2)

green_label = ct.CTkLabel(master=root, text="Green").grid(row=1, column=0)
SliderG = ct.CTkSlider(master=root, from_=-255 , to=255)
SliderG.grid(row=1, column=1, columnspan=2)

blue_label = ct.CTkLabel(master=root, text="Blue").grid(row=2, column=0)
SliderB = ct.CTkSlider(master=root, from_=-255 , to=255)
SliderB.grid(row=2, column=1, columnspan=2)

button_reset = ct.CTkButton(master=root, text="Reset", command=lambda: reset_Slider()).grid(row=4, column=0,padx=30,pady=8)

im = Image.fromarray(ex_img)
imgtk = ImageTk.PhotoImage(image=im)
imageViewed = ct.CTkLabel(master=root, image=imgtk).grid(row=0, column=3, rowspan=4, columnspan=4, padx=20, pady=5)

def run_film(fps):
    forward(number+1)
    threading.Timer(1/fps, lambda: run_film(fps)).start()

run_film(16)

root.mainloop()
from tkinter import *
import cv2
import numpy as np

w,h = 640,480


def controller(img,  brightness=255, contrast=127):

	brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
	contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))

	if brightness != 0:
		if brightness > 0:

			shadow = brightness
			max = 255
		else:
			shadow = 0
			max = 255 + brightness

		al_pha = (max - shadow) / 255
		ga_mma = shadow

		cal = cv2.addWeighted(img, al_pha, img, 0, ga_mma)

	else:
		cal = img

	if contrast != 0:
		Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
		Gamma = 127 * (1 - Alpha)

		cal = cv2.addWeighted(cal, Alpha, cal, 0, Gamma)

	return cal

def callimage(num):

    path = "colors/frame" + str(num) + ".jpg"
    frame = cv2.imread(path)
    frame = cv2.resize(frame,(int(frame.shape[1]*0.4),int(frame.shape[0]*0.4)))

    # brightness = alpha
    # contrast = cont

    # effect = controller(frame, brightness, contrast)

    cv2.imshow("test",frame) 

def forward(img_no):

    global button_forward
    global button_back
    global number
    number = img_no

    callimage(img_no)

    button_for = Button(root, text="Forward", command= lambda: forward(img_no+1))
    button_back = Button(root, text="Back", command= lambda: back(img_no-1))
    
    button_back.grid(row=3, column=0)
    button_for.grid(row=3, column=2)

def back(img_no):

    global button_forward
    global button_back
    global number
    number = img_no

    callimage(img_no)

    button_for = Button(root, text="Forward", command=lambda: forward(img_no+1))
    button_back = Button(root, text="Back", command=lambda: back(img_no-1))

    button_back.grid(row=3, column=0)
    button_for.grid(row=3, column=2)

def show_values():
    print (SliderR.get(), SliderG.get(), SliderB.get())


root =Tk()

root.title("Visionneuse Numérique")

root.resizable(0,0)

# First Image to display
number = 0
callimage(number)

# Buttons
button_back = Button(root, text="Back",command=back, state= DISABLED).grid(row=3, column=0,padx=30,pady=8)  
button_forward = Button(root, text="Forward", command=lambda: forward(number+1)).grid(row=3, column=2)
button_refesh = Button(root, text="Refresh", command=lambda: callimage(number)).grid(row=3, column=1)
button_exit = Button(root, text="Exit", command=root.quit).grid(row=4, column=1,padx=30,pady=8)
button_show = Button(root, text="Show", command=show_values).grid(row=4, column=0,padx=30,pady=8)

red_label = Label(root, text="Red").grid(row=0, column=0)
SliderR = Scale(root, from_=0 , to=100, orient=HORIZONTAL, length=300)
SliderR.grid(row=0, column=1, columnspan=2)

green_label = Label(root, text="Green").grid(row=1, column=0)
SliderG = Scale(root, from_=0 , to=100, orient=HORIZONTAL, length=300)
SliderG.grid(row=1, column=1, columnspan=2)

blue_label = Label(root, text="Blue").grid(row=2, column=0)
SliderB = Scale(root, from_=0 , to=100, orient=HORIZONTAL, length=300)
SliderB.grid(row=2, column=1, columnspan=2)

alpha_label = Label(root, text="Alpha").grid(row=5, column=0)
alpha = Scale(root, from_=-255 , to=255, orient=HORIZONTAL, length=300)
alpha.grid(row=5, column=1, columnspan=2)

cont_label = Label(root, text="Contrast").grid(row=6, column=0)
cont = Scale(root, from_=-127 , to=127, orient=HORIZONTAL, length=300)
cont.grid(row=6, column=1, columnspan=2)

root.mainloop()
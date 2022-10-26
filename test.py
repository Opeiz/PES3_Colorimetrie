from tkinter import *
import cv2

w,h = 640,480
print(h,w)

def callimage(num):
    path = "frames/frame" + str(num) + ".jpg"
    frame = cv2.imread(path)
    frame = cv2.resize(frame,(w,h))
    cv2.imshow("test",frame) 

def forward(img_no):

    global button_forward
    global button_back
    global button_exit

    callimage(img_no)

    button_for = Button(root, text="Forward", command= lambda: forward(img_no+1))
    button_back = Button(root, text="Back", command= lambda: back(img_no-1))
    
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_for.grid(row=1, column=2)


def back(img_no):

    global button_forward
    global button_back
    global button_exit

    callimage(img_no)

    button_for = Button(root, text="Forward", command=lambda: forward(img_no+1))
    button_back = Button(root, text="Back", command=lambda: back(img_no-1))

    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_for.grid(row=1, column=2)


root =Tk()

root.title("Visionneuse Numérique")

root.geometry("500x500")

root.columnconfigure(0,weight=2)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=2)
root.rowconfigure(0,weight=2)
root.rowconfigure(1,weight=2)
root.rowconfigure(2,weight=2)
root.rowconfigure(3,weight=2)

callimage(0)

button_back = Button(root, text="Back",command=back)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text="Forward", command=lambda: forward(1))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
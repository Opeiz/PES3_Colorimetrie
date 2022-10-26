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

    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = Label(image=callimage(img_no))

    button_for = Button(root, text="Forward", command=lambda: forward(img_no+1))
    button_back = Button(root, text="Back", command=lambda: back(img_no-1))

    # button_back.pack()
    # button_exit.pack()
    # button_for.pack()


def back(img_no):

    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = Label(image=callimage(img_no))

    button_for = Button(root, text="Forward", command=lambda: forward(img_no + 1))
    button_back = Button(root, text="Back", command=lambda: back(img_no - 1)) 

    # button_back.pack()
    # button_exit.pack()
    # button_for.pack()


root =Tk()

root.title("Visionneuse Numérique")

root.geometry("500x500")

label = Label(image=callimage(0))

button_back = Button(root, text="Back", bd = "5",command=back)

button_exit = Button(root, text="Exit",bd = "5", command=root.quit)

button_forward = Button(root, text="Forward",bd = "5", command=lambda: forward(1))

button_back.pack()
button_exit.pack()
button_forward.pack()

root.mainloop()
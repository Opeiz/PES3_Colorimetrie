from cgi import test
from tkinter import *
from turtle import left

main = Tk()

main.resizable()
main.title('Visionneuse Numérique')
Label(main,text="Prévisualisation", font=('bold',12)).pack()

Frames = Frame(main,width=960,height=540,bg='white')
Frames.pack()

Button(main, text = 'Back', command = Back, bg= ' light blue ').place(x = 240, y = 50)  
Button(main, text = 'Next', command = Next, bg = ' light blue ').place(x = 1010, y = 50)  


main.mainloop()
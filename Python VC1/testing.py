import tkinter as tk
import random
from tkinter import messagebox


listCircle =[]
circleToPop = [] #the index of the circles to remove because they are out of the screen
#function that creates the circle on the top of my screen and add it to the list of circles
def createCircle(event):
    global listCircleUpToDown
    x = random.randrange(0,550)
    y = 0
    size = 50
    circle = canvas.create_oval(x, y, x+size, y+size, fill = "red")
    listCircle.append(circle)

#function to move the circles created

def moveCircles():
    global listCircle, circleToPop
    for i in range(len(listCircle)):
        circle = listCircle[i]
        y = canvas.coords(circle)[1]
        if y < 600:
            canvas.move(circle, 0, 10)
        else:
            circleToPop.append(i)
            canvas.delete(circle)
    for index in sorted(circleToPop, reverse=True):
        listCircle.pop(index)
    circleToPop = []
    canvas.after(50, lambda:moveCircles())







SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PNC Shoot'em up game in Python"

root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
frame = tk.Frame()
frame.master.title("Shoot'em up in TK")
frame.pack(expand=True, fill='both')
canvas = tk.Canvas(frame)
canvas.pack(expand=True, fill='both')


moveCircles() #I run the qnimqtion of circles

root.bind("<space>", createCircle)
root.mainloop()
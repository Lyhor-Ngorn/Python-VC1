from tkinter import *
root=Tk()
root.geometry('1200x600')
root.resizable(False,False)
root.title('Hello the best team')
canvas=Canvas()
canvas.configure(bg='black')








#The ship movement
def moveLeft(event):
    global ourShip
    x,y=canvas.coords(ourShip)
    if x>70:
        canvas.move(ourShip,-10,0)
        canvas.move(shooting1,-10,0)
        canvas.move(shooting2,-10,0)
def moveRight(event):
    global ourShip
    x,y=canvas.coords(ourShip)
    if x<1200:
        canvas.move(ourShip,10,0)
        canvas.move(shooting2,10,0)
        canvas.move(shooting1,10,0)
def moveUp(event):
    global ourShip
    x,y=canvas.coords(ourShip)
    if y>0 and y<=600:
        canvas.move(ourShip,0,-10)
        canvas.move(shooting1,0,-10)
        canvas.move(shooting2,0,-10)
def moveDown(event):
    global ourShip
    x,y=canvas.coords(ourShip)
    if y>=0 and y<=520:
        canvas.move(ourShip,0,10)
        canvas.move(shooting2,0,10)
        canvas.move(shooting1,0,10)
def shooting(event):
    global shooting1,shooting2
    x3,y3=canvas.coords(shooting2)
    canvas.move(shooting1,0,-10)
    canvas.move(shooting2,0,-10)
    canvas.after(10,lambda:shooting(event))











#our ship
bullet=PhotoImage(file='VC1/bullet_resize.png')
shooting1=canvas.create_image(545,430,image=bullet,anchor=NE)
shooting2=canvas.create_image(505,430,image=bullet,anchor=NE)
ship=PhotoImage(file = "VC1/spaceship.png", name = "mouse_pointer",)
ourShip=canvas.create_image(550,400,image=ship,anchor=NE)










#action of the ship 
root.bind('<Left>',moveLeft)
root.bind('<Right>',moveRight)
root.bind('<Up>',moveUp)
root.bind('<Down>',moveDown)
root.bind('<Button-1>',shooting)






#print on thhe tk canvas
canvas.pack(expand=True,fill='both')
root.mainloop() 
from tkinter import *
root=Tk()
root.geometry('1500x900')
root.resizable(False,False)
root.title('Hello the best team')
canvas=Canvas()
background=PhotoImage(file='VC1/BG.png')
canvas.create_image(750,400,image=background)


#The ship movement
def moveLeft(event):
    global ourShip
    x,y=canvas.coords(ourShip)
    if x>70:
        canvas.move(ourShip,-40,0)

def moveRight(event):
    global ourShip
    x,y=canvas.coords(ourShip)
    if x<1500:
        canvas.move(ourShip,40,0)

def moveUp(event):
    global ourShip
    x,y=canvas.coords(ourShip)
    if y>0:
        canvas.move(ourShip,0,-40)

def moveDown(event):
    global ourShip
    x,y=canvas.coords(ourShip)
    if y<800:
        canvas.move(ourShip,0,40)


def shoootingIt():
    canvas.move(shooting1,0,-20)
    canvas.move(shooting2,0,-20)

    y=canvas.coords(shooting1)[1]
    stopShooting = y <=0

    if not stopShooting:
        canvas.after(5,lambda:shoootingIt())
    else :
        canvas.delete(shooting1)
        canvas.delete(shooting2)
        shooting()
   

def shooting():
    global ourShip,shooting1,shooting2, bullet,alwayShoot,y1

    x1 = canvas.coords(ourShip)[0]
    y1 = canvas.coords(ourShip)[1]
    
    shooting1=canvas.create_image(x1-60,y1+35,image=bullet)
    shooting2=canvas.create_image(x1-2,y1+35,image=bullet)
    shoootingIt()






#our ship





bullet=PhotoImage(file='VC1/bullet_resize.png')
ship=PhotoImage(file = "VC1/spaceship.png", name = "mouse_pointer",)
ourShip=canvas.create_image(750,750,image=ship,anchor=NE)



#enermy






#action of the ship 
root.bind('<a>',moveLeft)
root.bind('<d>',moveRight)
root.bind('<w>',moveUp)
root.bind('<s>',moveDown)


shooting()






#print on thhe tk canvas
canvas.pack(expand=True,fill='both')
root.mainloop() 
from tkinter import *
from pygame import mixer
from playsound import playsound
root=Tk()
root.geometry('1500x900')
root.resizable(False,False)
root.title('Hello the best team')
canvas=Canvas()
background=PhotoImage(file='VC1/BG.png')
canvas.create_image(750,400,image=background)
soundObj = mixer.Sound('VC1/laser.wav')

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
        canvas.after(10,lambda:shoootingIt())
    else :
        canvas.delete(shooting1)
        canvas.delete(shooting2)
        shooting()
   

def shooting():
    global ourShip,shooting1,shooting2, bullet,y1
    x1 = canvas.coords(ourShip)[0]
    y1 = canvas.coords(ourShip)[1]
    shooting1=canvas.create_image(x1-60,y1+35,image=bullet)
    shooting2=canvas.create_image(x1-2,y1+35,image=bullet)
    ('VC1/laser.wav')
    shoootingIt()
def e_move(event):
    global enermy,eachEnermy,x,y
    x1=canvas.coords(eachEnermy)[0]
    y1=canvas.coords(eachEnermy)[1]
    if x1==1500:
        x=-x

    elif x1==0:
        x=-x
    canvas.move(eachEnermy,x,y)
    if y1>=900:
        canvas.delete(eachEnermy)
        canvas.after(10,lambda:createEnermy(event))
    else:
        canvas.after(10,lambda:e_move(event))
def createEnermy(event):
    global enermy,eachEnermy

    eachEnermy=canvas.create_image(200,0,image=e_ship)
    e_move(event)
def startEnermy(event):
    global text,enermy
    canvas.delete(text)
    createEnermy(event)









#our ship





bullet=PhotoImage(file='VC1/bullet_resize.png')
ship=PhotoImage(file = "VC1/spaceship.png", name = "mouse_pointer",)
ourShip=canvas.create_image(750,750,image=ship,anchor=NE)



#enermy
e_ship=PhotoImage(file='VC1/enermy.png')

x=5
y=3



#action of the ship 
root.bind('<a>',moveLeft)
root.bind('<d>',moveRight)
root.bind('<w>',moveUp)
root.bind('<s>',moveDown)
root.bind('<space>',startEnermy)

text=canvas.create_text(900,450,fill="white",font="Times 40 italic bold",text="Space to start game")





shooting()






#print on thhe tk canvas
canvas.pack(expand=True,fill='both')
root.mainloop() 
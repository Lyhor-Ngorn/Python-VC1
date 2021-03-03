from tkinter import *
from pygame import mixer
import random
from tkinter import messagebox

# CONSTANT  --------------------------------------------------------------------------------------------------

# GLOBAL VARIABLE --------------------------------------------------------------------------------------------------
listOfEnemy=[]
enrmyToPop=[]
stopGame=0
listOfShooting=[]
#  FUNCTION--------------------------------------------------------------------------------------------------



def moveLeft(event):
    global ourShip, stopGame
    if stopGame<=20000:
        x,y=canvas.coords(ourShip)
        if x>70:
            canvas.move(ourShip,-40,0)

def moveRight(event):
    global ourShip, stopGame
    if stopGame<=20000:
        x,y=canvas.coords(ourShip)
        if x<1500:
            canvas.move(ourShip,40,0)

def moveUp(event):
    global ourShip, stopGame
    if stopGame<=20000:
        x,y=canvas.coords(ourShip)
        if y>0:
            canvas.move(ourShip,0,-40)

def moveDown(event):
    global ourShip, stopGame
    if stopGame<=20000:
        x,y=canvas.coords(ourShip)
        if y<800:
            canvas.move(ourShip,0,40)




def shoootingIt():
    global stopGame
    if stopGame<=20000:
        canvas.move(shooting1,0,-40)
        canvas.move(shooting2,0,-40)
        y=canvas.coords(shooting1)[1]
        x=canvas.coords(shooting1)[0]
        stopShooting = y<0
        soundObj.play()
        if not stopShooting:
            canvas.after(50,lambda:shoootingIt())
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
    shoootingIt()




def createEnemy():
    global listOfEnemy,listOfShooting,enermy,stopGame
    x = random.randrange(0,1500)
    y = 0
    enermy=canvas.create_image(x,y,image=e_ship)
    listOfEnemy.append(enermy)
    if stopGame<=20000:
        canvas.after(1000, lambda:createEnemy())

# def makeBullet():
#     global enermy,bullet
#     x=canvas.coords(enermy)[0]
#     y=canvas.coords(enermy)[1]
#     bullet=canvas.create_image(x,y,image=lazer)



def enermyMove():
    global bullet,stopGame
    enrmyToPop = []

    for i in range(len(listOfEnemy)):
        circle = listOfEnemy[i]
        y = canvas.coords(circle)[1]
        
        if y < 950:
            canvas.move(circle, 0, 10)
        else:
            enrmyToPop.append(i)
    
    # delete ennemie if any ennemy to delete
    removeEnnemies(enrmyToPop)
    stopGame+=50
    if stopGame<=20000:
        canvas.after(50, lambda:enermyMove())
    else:
        canvas.create_text(700,400,fill="red",font="Times 90 italic bold",text="Game Over")

        canvas.delete(shooting1)
        canvas.delete(shooting2)



def removeEnnemies( ennemiesIndexes) :
    for enneyIndex in ennemiesIndexes:
        canvas.delete(enneyIndex)
        listOfEnemy.pop(enneyIndex)













#our ship

mixer.init(44100, -16,2,2048)
root=Tk()
root.geometry('1500x900')
root.resizable(False,False)
root.title('CRAZY PROJECT')
canvas=Canvas()
background=PhotoImage(file='VC1/BG.png')
canvas.create_image(750,400,image=background)
soundObj = mixer.Sound('VC1/laser.wav')


bullet=PhotoImage(file='VC1/bullet_resize.png')
ship=PhotoImage(file = "VC1/spaceship.png", name = "mouse_pointer",)
ourShip=canvas.create_image(750,750,image=ship,anchor=NE)



#enermy
e_ship=PhotoImage(file='VC1/enermy.png')
lazer=PhotoImage(file='VC1/redLaser.png')
# text=canvas.create_text(900,450,fill="white",font="Times 40 italic bold",text="Space to start game")




#action of the ship 
root.bind('<a>',moveLeft)
root.bind('<d>',moveRight)
root.bind('<w>',moveUp)
root.bind('<s>',moveDown)
# root.bind('<space>',startGame)






shooting()
createEnemy()
enermyMove()






#print on thhe tk canvas
canvas.pack(expand=True,fill='both')
root.mainloop() 
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 22:53:25 2020

@author: ishty
"""


#tic tac toe
import random
from tkinter import *
ttt = Tk()

ttt.minsize(width = 1000, height = 615)

papick = [] #player and ai picks on x or o

print (papick)

remslot = [1,2,3,4,5,6,7,8,9] #spots left to fill

tlayer = ['-','-','-'] #the tictactoe grid
mlayer = ['-','-','-']
blayer = ['-','-','-']

def papicker(a):
    if a == 'X':
        papick.append('X')
        papick.append('O')
        tttbutts()
    elif a == 'O':
        papick.append('O')
        papick.append('X')
        tttbutts()
    else:
        papick.append('Bruh game is messed')
        papick.append('Bruh game is messed')

def winninglist(t,m,b):
    win1l = [t[0], t[1], t[2]] #winning list
    win2l = [m[0], m[1], m[2]]
    win3l = [b[0], b[1], b[2]]
    win4l = [t[0], m[0], b[0]]
    win5l = [t[1], m[1], b[1]]
    win6l = [t[2], m[2], b[2]]
    win7l = [t[0], m[1], b[2]]
    win8l = [t[2], m[1], b[0]]
    winxl = [win1l,win2l,win3l,win4l,win5l,win6l,win7l,win8l]
    return winxl
    
winx = ['X','X','X']
wino = ['O','O','O']

#def winx():
    #winxl =[win1l,win2l,win3l,win4l,win5l,win6l,win7l,win8l]
def wonlabel():
    w = Label(ttt, text="YOU WON!", width=1000, height= 615)
    
    
def winvalx(x): #checks if you won yet or not
    if (x=='X'):
        if winx in winninglist(tlayer,mlayer,blayer):
            for _ in ttt.winfo_children():
                _.destroy()  
            w = Label(ttt, text="YOU WON!", width=16, height= 9)
            w.pack(anchor='center')
        elif wino in winninglist(tlayer,mlayer,blayer):
            for _ in ttt.winfo_children():
                _.destroy()  
            w = Label(ttt, text="YOU LOST!", width=16, height= 9)
            w.pack(anchor='center')
    if (x=='O'):
        if wino in winninglist(tlayer,mlayer,blayer):
            for _ in ttt.winfo_children():
                _.destroy()  
            w = Label(ttt, text="YOU WON!", width=16, height= 9)
            w.pack(anchor='center')
        elif winx in winninglist(tlayer,mlayer,blayer):
            for _ in ttt.winfo_children():
                _.destroy()  
            w = Label(ttt, text="YOU LOST!", width=16, height= 9)
            w.pack(anchor='center')
def winvaly(x): #checks if you won yet or not
    if (x=='X'):
        if winx in winninglist(tlayer,mlayer,blayer):
            for _ in ttt.winfo_children():
                _.destroy()  
            w = Label(ttt, text="YOU LOST!", width=16, height= 9)
            w.pack(anchor='center')
        elif wino in winninglist(tlayer,mlayer,blayer):
            for _ in ttt.winfo_children():
                _.destroy()  
            w = Label(ttt, text="YOU WON!", width=16, height= 9)
            w.pack(anchor='center')
    if (x=='O'):
        if wino in winninglist(tlayer,mlayer,blayer):
            for _ in ttt.winfo_children():
                _.destroy()  
            w = Label(ttt, text="YOU LOST!", width=16, height= 9)
            w.pack(anchor='center')
        elif winx in winninglist(tlayer,mlayer,blayer):
            for _ in ttt.winfo_children():
                _.destroy()  
            w = Label(ttt, text="YOU WON!", width=16, height= 9)
            w.pack(anchor='center')

def des(x): #button destroyer
    x.destroy()

def btx(bt,x): #Button text updater for X
    if (papick[0]=='X') and x in remslot:
        bt.configure(text='X')
        remslot.remove(x)
    if (papick[0]=='O')and x in remslot:
        bt.configure(text='O')
        remslot.remove(x)
    else:
        pass

def bty(bt,x):
    if (papick[1]=='X') and x in remslot:
        bt.configure(text='X')
        remslot.remove(x)
    if (papick[1]=='O')and x in remslot:
        bt.configure(text='O')
        remslot.remove(x)
    else:
        pass    


def btd(bt): #Button disabler
    bt.configure(state='disabled')
    
# def bte(bt): #Button enablr
#     bt.configure(state='normal', text=tlayer[1])
    
def grider(but, r, c): #positions the buttons by row and column
    but.grid(row=r,column=c)
        
def inputer(a,b,c,x):
    if x in remslot:
        if a == 1:  #a picks out the layers and b picks out the position and c is picked weapon x validate usage 
            if b == 1:
                tlayer[0]=c
            elif b == 2:
                tlayer[1]=c
            elif b == 3:
                tlayer[2]=c     
        elif a == 2:
            if b == 1:
                mlayer[0]=c
            elif b == 2:
                mlayer[1]=c
            elif b == 3:
                mlayer[2]=c
        elif a == 3:
            if b == 1:
                blayer[0]=c
            elif b == 2:
                blayer[1]=c
            elif b == 3:
                blayer[2]=c
    else:
        pass
    
def but3com(a,b,x,y): #ttt button commands
    inputer(a, b, papick[0], x)
    btx(y, x)
    winvalx(papick[0])
    btd(y)
    ran = random.choice(remslot)
    butdict = {1:[1,1,1,onebut],2:[1,2,2,twobut],3:[1,3,3,threebut],4:[2,1,4,fourbut],5:[2,2,5,fivebut],6:[2,3,6,sixbut],7:[3,1,7,sevenbut],8:[3,2,8,eightbut],9:[3,3,9,ninebut]}
    inputer(butdict[ran][0], butdict[ran][1], papick[1], ran)
    bty(butdict[ran][3], ran)
    winvaly(papick[1])
    btd(butdict[ran][3])

           
def tttbutts(): # stage 3 // 
    
    print(papick[0])
    print(tlayer[0])
    
    des(ixbutton)
    des(iobutton)
    
    global onebut
    onebut = Button(ttt, text=tlayer[0], padx = 160, pady = 90)
    onebut['command']= lambda : but3com(1, 1, 1, onebut) 
    grider(onebut,0,0)

    global twobut
    twobut = Button(ttt, text=tlayer[1], padx = 160, pady = 90)
    twobut['command']= lambda : but3com(1, 2, 2, twobut)
    grider(twobut,0,1)
    
    global threebut
    threebut = Button(ttt, text=tlayer[2], padx = 160, pady = 90)
    threebut['command']= lambda : but3com(1, 3, 3, threebut)
    grider(threebut,0,2)
    
    global fourbut
    fourbut = Button(ttt, text=mlayer[0], padx = 160, pady = 90)
    fourbut['command']= lambda : but3com(2, 1, 4, fourbut)
    grider(fourbut,1,0)
    
    global fivebut
    fivebut = Button(ttt, text=mlayer[1], padx = 160, pady = 90)
    fivebut['command']= lambda : but3com(2, 2, 5, fivebut)
    grider(fivebut,1,1)
    
    global sixbut
    sixbut = Button(ttt, text=mlayer[2], padx = 160, pady = 90)
    sixbut['command']= lambda : but3com(2, 3, 6, sixbut)
    grider(sixbut,1,2)
    
    global sevenbut
    sevenbut = Button(ttt, text=blayer[0], padx = 160, pady = 90)
    sevenbut['command']= lambda : but3com(3, 1, 7, sevenbut)
    grider(sevenbut,2,0)
    
    global eightbut
    eightbut = Button(ttt, text=blayer[1], padx = 160, pady = 90)
    eightbut['command']= lambda : but3com(3, 2, 8, eightbut)
    grider(eightbut,2,1)
    
    global ninebut
    ninebut = Button(ttt, text=blayer[2], padx = 160, pady = 90)
    ninebut['command']= lambda : but3com(3, 3, 9, ninebut)
    grider(ninebut,2,2)
    
def xo(): #stage two //lets the user pick x or o as their pick
    
    des (startbutton)
    
    global ixbutton       
    ixbutton = Button(ttt, text='X', padx = 160, pady = 90)
    ixbutton['command'] = lambda : papicker('X')
    ixbutton.grid(row=0,column=0)
    
    global iobutton
    iobutton = Button(ttt, text='O', padx = 160, pady = 90)
    iobutton['command'] = lambda : papicker('O')
    iobutton.grid(row=0,column=1)
    
def stb(): #stage1 //has start button
    
    global startbutton
    startbutton = Button(ttt, text="Start", command = xo)
    startbutton.grid(row=1,column=2)
    
   
    

stb()


ttt.mainloop()
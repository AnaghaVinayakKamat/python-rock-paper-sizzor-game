#import modules

from tkinter import *
from random import *

#initialize the window
root = Tk()                                            
root.geometry('500x400')            
root.resizable(0,0)                           
root.title('Rock,Paper,Sizzors Game')
root.config(bg ='black')
Label(root, text = 'Rock, Paper ,Sizzors' , font='arial 20 bold', bg = 'white').place(x=100,y=0)

#computer1 choice

comp1_pick= choice(['rock', 'paper', 'sizzor'])

# computer2 choice

comp2_pick= choice(['rock', 'paper', 'sizzor'])

#function def
def play():
    if(comp1_pick =='rock' and comp2_pick =='paper'):
        print('Computer 1 chose:',comp1_pick)
        print('Computer 2 chose:',comp2_pick)
        print('Computer 2 wins')
    elif(comp1_pick =='rock' and comp2_pick =='sizzor'):
        print('Computer 1 chose:',comp1_pick)
        print('Computer 2 chose:',comp2_pick)
        print('Computer 1 wins')
    elif(comp1_pick =='paper' and comp2_pick =='rock'):
        print('Computer 1 chose:',comp1_pick)
        print('Computer 2 chose:',comp2_pick)
        print('Computer 1 wins')
    elif(comp1_pick =='paper' and comp2_pick =='sizzor'):
        print('Computer 1 chose:',comp1_pick)
        print('Computer 2 chose:',comp2_pick)
        print('Computer 2 wins')
    elif(comp1_pick =='sizzor' and comp2_pick =='rock'):
        print('Computer 1 chose:',comp1_pick)
        print('Computer 2 chose:',comp2_pick)
        print('Computer 2 wins')
    elif(comp1_pick =='sizzor' and comp2_pick =='paper'):
        print('Computer 1 chose:',comp1_pick)
        print('Computer 2 chose:',comp2_pick)
        print('Computer 1 wins')
    elif(comp1_pick =='rock' and comp2_pick =='rock'):
        print('Computer 1 chose:',comp1_pick)
        print('Computer 2 chose:',comp2_pick)
        print("It's a tie")
    elif(comp1_pick =='paper' and comp2_pick =='paper'):
        print('Computer 1 chose:',comp1_pick)
        print('Computer 2 chose:',comp2_pick)
        print("It's a tie")
    elif(comp1_pick =='sizzor' and comp2_pick =='sizzor'):
        print('Computer 1 chose:',comp1_pick)
        print('Computer 2 chose:',comp2_pick)
        print("It's a tie")

#buttons
Label(root, text = 'Check the button to generate the game' , font='arial 15 bold', anchor= 'center', fg = 'yellow', bg='black').place(x = 65,y=40)
game=Button(root, text='Start The Game', font='arial 30 bold', bg='black', fg='orange', command=play).place(x=90 , y=120)

root.mainloop()

#import modules

from tkinter import *
import random

#initialize the window
root = Tk()                                            
root.geometry('500x400')            
root.resizable(0,0)                           
root.title('Rock,Paper,Sizzors Game')
root.config(bg ='black')
Label(root, text = 'Rock, Paper ,Sizzors' , font='arial 20 bold', bg = 'white').place(x=100,y=0)

#user choice heading
user_pick= StringVar()
Label(root, text = 'choose any one: rock, paper ,sizzor' , font='arial 15 bold', anchor= 'center', fg = 'yellow', bg='black').place(x = 65,y=40)

#computer choice
comp_pick = random.randint(1,3)

if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'sizzor'

#function def

def play():

    if (user_pick == comp_pick):
        print('tie,you both select same')
        
    elif (user_pick == 'rock' and comp_pick == 'paper'):
        print('you loose,computer select paper')
        
    elif (user_pick == 'rock' and comp_pick == 'sizzor'):
        print('you win,computer select sizzor')
        
    elif (user_pick == 'paper' and comp_pick == 'sizzor'):
        print('you loose,computer select sizzor')
        
    elif (user_pick == 'paper' and comp_pick == 'rock'):
        print('you win,computer select rock')
        
    elif (user_pick == 'sizzor' and comp_pick == 'rock'):
        print('you loose,computer select rock')

    else:
        print('you win ,computer select paper')
        
#Selection buttons

Button(root, text='rock', font='arial 30 bold', command=play, bg='black', fg='orange').place(x=40 , y=90)
Button(root, text='paper', font='arial 30 bold', command=play, bg='black', fg='orange').place(x=170 , y=90)
Button(root, text='sizzor', font='arial 30 bold', command=play, bg='black', fg='orange').place(x=320 , y=90)

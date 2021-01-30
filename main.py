from tkinter import Tk, Label, Button, PhotoImage, RIDGE
import tkinter.messagebox as msg
import random

# Variables for Selction
userSelected = ''
computerSelected = ''

# Functions
def Result(userSelect, computerSelect):
   if userSelect == computerSelect:
      result = 'Draw'
      Label(root, text=f'\nYou Selected: {userSelect}', font='Arial 12', bg='White', padx=40).place(x=40, y=120)
      Label(root, text=f'\nComputer Selected: {computerSelect}', font='Arial 12', bg='white', padx=40).place(x=40, y=160)
      Label(root, text=f'\nResult: {result}', font='Arial 12', bg='White', padx=65).place(x=15, y=200)

   elif userSelect == 'Rock' and computerSelect == 'Paper':
      result = 'Computer Won' 
      Label(root, text=f'\nYou Selected: {userSelect}', font='Arial 12', bg='White', padx=40).place(x=40, y=120)
      Label(root, text=f'\nComputer Selected: {computerSelect}', font='Arial 12', bg='White', padx=40).place(x=40, y=160)
      Label(root, text=f'\nResult: {result}', font='Arial 12', bg='White', padx=40).place(x=40, y=200)
   
   elif userSelect == 'Paper' and computerSelect == 'Scissor':
      result = 'Computer Won'
      Label(root, text=f'\nYou Selected: {userSelect}', font='Arial 12', bg='White', padx=40).place(x=40, y=120)
      Label(root, text=f'\nComputer Selected: {computerSelect}', font='Arial 12', bg='White', padx=40).place(x=40, y=160)
      Label(root, text=f'\nResult: {result}', font='Arial 12', bg='White', padx=40).place(x=40, y=200)

   elif userSelect == 'Scissor' and computerSelect == 'Rock':
      result = 'Computer Won'
      Label(root, text=f'\nYou Selected: {userSelect}', font='Arial 12', bg='White', padx=40).place(x=40, y=120)
      Label(root, text=f'\nComputer Selected: {computerSelect}', font='Arial 12', bg='White', padx=40).place(x=40, y=160)
      Label(root, text=f'\nResult: {result}', font='Arial 12', bg='White', padx=40).place(x=40, y=200)

   else:
      result = 'You Won'
      Label(root, text=f'\nYou Selected: {userSelect}', font='Arial 12', bg='White', padx=40).place(x=40, y=120)
      Label(root, text=f'\nComputer Selected: {computerSelect}', font='Arial 12', bg='White', padx=40).place(x=40, y=160)
      Label(root, text=f'\nResult: {result}', font='Arial 12', bg='White', padx=40).place(x=40, y=200)

def rock():
   global userSelected
   global computerSelected
   userSelected='Rock'
   list = ['Rock','Paper','Scissor']
   choice = random.choice(list)
   computerSelected=choice
   Result(userSelected, computerSelected)

def paper():
   global userSelected
   global computerSelected
   userSelected='Paper'
   list = ['Rock','Paper','Scissor']
   choice = random.choice(list)
   computerSelected=choice
   Result(userSelected, computerSelected)

def scissor():
   global userSelected
   global computerSelected
   userSelected='Scissor'
   list = ['Rock','Paper','Scissor']
   choice = random.choice(list)
   computerSelected=choice
   Result(userSelected, computerSelected)

def leave():
   ask=msg.askyesno('Exit', 'Do you want to exit the game?')
   if ask == True:
      root.destroy()

# Basic Tkinter Setup
root = Tk()
root.geometry('500x300')
root.minsize(500, 300)
root.maxsize(500, 300)
root.configure(bg='white')
photo = PhotoImage(file='icon.png')
root.iconphoto(False, photo)
root.title('Rock, Paper & Scissor')
Label(text='Select Your Choice!\n\n', font='arial 15', bg='white',pady=10).pack()

# Rock, Paper and Scissor Buttons
rock_button = Button(root, text='Rock', padx=10, pady=10, relief=RIDGE, bg='Yellow', font='Aquatico, 15', command=rock)
paper_button = Button(root, text='Paper', padx=10, pady=10, relief=RIDGE, bg='Yellow', font='Aquatico, 15', command=paper)
scissor_button = Button(root, text='Scissor', padx=10, pady=10, relief=RIDGE, bg='Yellow', font='Aquatico, 15', command=scissor)

# Placing Buttons
rock_button.place(x=50, y=50)
paper_button.place(x=190, y=50)
scissor_button.place(x=340, y=50)

# Exit Button
Button(root, text='Exit', padx=2, pady=2, font='Arial 10', bg='Red', fg='White', command=leave).pack(anchor='se', side='bottom')
root.mainloop()

# Github: musab-sayyed
# Instagram: _musab.programmer
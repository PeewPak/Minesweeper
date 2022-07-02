from tkinter import *
import random
#24*30=720

size = 24
bombs = 70
buttons = [[None]*size]*size
fields = [[None]*size]*size

root = Tk()
root.geometry("720x720")
root.resizable(False, False)
pixelVirtual = PhotoImage(width=1, height=1)

class Field:
    def __init__(self, bomb, neighbour):
        self.bomb = bomb
        self.neighbour = neighbour

    def Explosive(self):
        self.bomb = True
        self.neighbour = 0

    def Safe(self, near):
        self.bomb = False
        self.neighbour = near

def choose_bomb():
    x = random.randint(0, size-1)

    return(x)

for x in range(size):
    for y in range(size):
        buttons[x][y] = Button(root ,image=pixelVirtual, width=30, height=30, compound="c")
        fields[x][y] = Field(False, 0)
        buttons[x][y].grid(row = x, column = y)

for i in range(bombs):
    x = choose_bomb()
    y = choose_bomb()

    while fields[x][y].bomb == True:
        x = choose_bomb()
        y = choose_bomb()
    else:
        fields[x][y].Explosive

for x in range(size):
    for y in range(size):
        if fields[x][y].bomb == False:
            fields[x][y].Safe


root.mainloop()
import turtle
import random
import time

#setting up the screen, and it's properties
screen=turtle.getscreen()
screen.colormode(255)
#screen.bgcolor("black")
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", 1)

turtle.ht() #hides the og turtle

screen.tracer(0) # stops time

def making_board():
    no_rows=10
    no_cols=10
    no_squares=no_rows*no_cols
    starting_position=50
    no_mines = 0.1*no_squares

    board = [["    " for i in range(no_cols)] for i in range(no_rows)]
    mines=[]

    while len(mines)<no_mines:
        random_position = random.randint(0,no_squares-1)
        j=0
        found=False
        while j<len(mines) and not found:
            if mines[j]==random_position or random_position==starting_position:
                found=True
            j+=1
        if not found:
            mines.append(random_position)

    for i in range(len(mines)):
        board[mines[i]//no_rows][mines[i]%no_cols]='mine'
    
    return board

board = making_board()

def show_board_for_testing(board):
    for i in range(len(board)):
        print(board[i])

show_board_for_testing(board)

screen.mainloop()
import turtle
import random
import time

#setting up the screen, and it's properties
screen=turtle.getscreen()
screen.colormode(255)
screen.bgcolor("#bdfff9")
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", 1)

canvas = turtle.getcanvas()
cursor_x, cursor_y = canvas.winfo_pointerx(), canvas.winfo_pointery()
width = screenTk.winfo_screenwidth()
height = screenTk.winfo_screenheight()

turtle.ht() #hides the og turtle

screen.tracer(0) # stops time

test=turtle.Turtle()
#test.ht()
test.up()
test.goto(0, 300)

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

def show_board_for_testing(board):
    for i in range(len(board)):
        print(board[i])

def display_board(board):
    no_rows=len(board)
    no_cols=len(board[0])

    square_size=50

    drawing_board=turtle.Turtle()
    drawing_board.ht()
    drawing_board.up()

    for i in range(no_cols*no_rows):
        square_centre=[(no_cols-1)*(-square_size/2)+((i%no_cols)*square_size), (no_rows-1)*(square_size/2)-((i//no_rows)*square_size)]

        drawing_board.goto(square_centre[0]-square_size/2, square_centre[1]+square_size/2)

        if ((i%2==0 and i%20<10) or (i%2==1 and i%20>10)):
            drawing_board.fillcolor("#d2e48a")
        else:
            drawing_board.fillcolor("#a2d149")

        drawing_board.down()
        drawing_board.begin_fill()
        drawing_board.setx(drawing_board.xcor()+square_size)
        drawing_board.sety(drawing_board.ycor()-square_size)
        drawing_board.setx(drawing_board.xcor()-square_size)
        drawing_board.sety(drawing_board.ycor()+square_size)
        drawing_board.end_fill()
        drawing_board.up()

    screen.update()

def main(board):
    screen.tracer(0)
    cursor_x, cursor_y = canvas.winfo_pointerx(), canvas.winfo_pointery()
    x, y = cursor_x, cursor_y
    test.write(cursor_x, cursor_y)

    time.sleep(10)
    test.clear()
    test.goto(0, 300)

    screen.update()
    screen.ontimer(lambda: main(board), 20)

board = making_board()
#show_board_for_testing(board)
display_board(board)


main(board)
screen.mainloop()
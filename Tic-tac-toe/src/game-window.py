# Tic-Tac-Toe game
# Modified code from https://copyassignment.com/tic-tac-toe-using-python-project-with-source-code/

from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox

root = Tk()
root.title('Tic-Tac-Toe')

click = True
count = 0

button1 = StringVar()
button2 = StringVar()
button3 = StringVar()
button4 = StringVar()
button5 = StringVar()
button6 = StringVar()
button7 = StringVar()
button8 = StringVar()
button9 = StringVar()

iconX = Image.open('cross.png')
xResized = iconX.resize((180, 200))
xTk = ImageTk.PhotoImage(xResized)

iconO = Image.open('circle.png')
oResized = iconO.resize((180, 200))
oTk = ImageTk.PhotoImage(oResized)


# Grid layout
def start():
    btn1 = Button(root, height=13, width=25, bd=1, relief='sunken', bg='white', textvariable=button1,
                  command=lambda: press(1, 0, 0))
    btn1.grid(row=0, column=0)

    btn2 = Button(root, height=13, width=25, bd=1, relief='sunken', bg='white', textvariable=button2,
                  command=lambda: press(2, 0, 1))
    btn2.grid(row=0, column=1)

    btn3 = Button(root, height=13, width=25, bd=1, relief='sunken', bg='white', textvariable=button3,
                  command=lambda: press(3, 0, 2))
    btn3.grid(row=0, column=2)

    btn4 = Button(root, height=13, width=25, bd=1, relief='sunken', bg='white', textvariable=button4,
                  command=lambda: press(4, 1, 0))
    btn4.grid(row=1, column=0)

    btn5 = Button(root, height=13, width=25, bd=1, relief='sunken', bg='white', textvariable=button5,
                  command=lambda: press(5, 1, 1))
    btn5.grid(row=1, column=1)

    btn6 = Button(root, height=13, width=25, bd=1, relief='sunken', bg='white', textvariable=button6,
                  command=lambda: press(6, 1, 2))
    btn6.grid(row=1, column=2)

    btn7 = Button(root, height=13, width=25, bd=1, relief='sunken', bg='white', textvariable=button7,
                  command=lambda: press(7, 2, 0))
    btn7.grid(row=2, column=0)

    btn8 = Button(root, height=13, width=25, bd=1, relief='sunken', bg='white', textvariable=button8,
                  command=lambda: press(8, 2, 1))
    btn8.grid(row=2, column=1)

    btn9 = Button(root, height=13, width=25, bd=1, relief='sunken', bg='white', textvariable=button9,
                  command=lambda: press(9, 2, 2))
    btn9.grid(row=2, column=2)


# Label buttons as X or O
def press(number, row, column):
    global click, count
    if click:
        labelIcon = Label(root, image=xTk)
        labelIcon.grid(row=row, column=column)
        match number:
            case 1:
                button1.set('X')
            case 2:
                button2.set('X')
            case 3:
                button3.set('X')
            case 4:
                button4.set('X')
            case 5:
                button5.set('X')
            case 6:
                button6.set('X')
            case 7:
                button7.set('X')
            case 8:
                button8.set('X')
            case _:
                button9.set('X')
        count += 1
        click = False
        checkWinner()
    else:
        labelIcon = Label(root, image=oTk)
        labelIcon.grid(row=row, column=column)
        match number:
            case 1:
                button1.set('O')
            case 2:
                button2.set('O')
            case 3:
                button3.set('O')
            case 4:
                button4.set('O')
            case 5:
                button5.set('O')
            case 6:
                button6.set('O')
            case 7:
                button7.set('O')
            case 8:
                button8.set('O')
            case _:
                button9.set('O')
        count += 1
        click = True
        checkWinner()


# Check if there's a winner
def checkWinner():
    global count, click
    if (
            (button1.get() == 'X' and button2.get() == 'X' and button3.get() == 'X')
            or (button4.get() == 'X' and button5.get() == 'X' and button6.get() == 'X')
            or (button7.get() == 'X' and button8.get() == 'X' and button9.get() == 'X')
            or (button1.get() == 'X' and button4.get() == 'X' and button7.get() == 'X')
            or (button2.get() == 'X' and button5.get() == 'X' and button8.get() == 'X')
            or (button3.get() == 'X' and button6.get() == 'X' and button9.get() == 'X')
            or (button1.get() == 'X' and button5.get() == 'X' and button9.get() == 'X')
            or (button3.get() == 'X' and button5.get() == 'X' and button7.get() == 'X')):
        tkinter.messagebox.showinfo('Winner', 'Player X wins !')
        click = True
        count = 0
        clear()
        start()
    elif (
            (button1.get() == 'O' and button2.get() == 'O' and button3.get() == 'O')
            or (button4.get() == 'O' and button5.get() == 'O' and button6.get() == 'O')
            or (button7.get() == 'O' and button8.get() == 'O' and button9.get() == 'O')
            or (button1.get() == 'O' and button4.get() == 'O' and button7.get() == 'O')
            or (button2.get() == 'O' and button5.get() == 'O' and button8.get() == 'O')
            or (button3.get() == 'O' and button6.get() == 'O' and button9.get() == 'O')
            or (button1.get() == 'O' and button5.get() == 'O' and button9.get() == 'O')
            or (button3.get() == 'X' and button5.get() == 'X' and button7.get() == 'X')):
        tkinter.messagebox.showinfo('Winner', 'Player O wins !')
        count = 0
        clear()
        start()
    elif count == 9:
        tkinter.messagebox.showinfo('Tie', 'Nobody wins!')
        click = True
        count = 0
        clear()
        start()


# Restarting the game
def clear():
    button1.set('')
    button2.set('')
    button3.set('')
    button4.set('')
    button5.set('')
    button6.set('')
    button7.set('')
    button8.set('')
    button9.set('')


start()
root.mainloop()

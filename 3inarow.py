from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter import Button
from tkinter import Tk
from tkinter import DISABLED



root = Tk()
root.title('3-in-a-ROW')
root.geometry("330x370")



click = True
count = 0


def newgame():
    global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9
    global clicked ,count
    clicked = True
    count = 0

    
    btn1 = Button(root, text=" ", font=("Gill Sans", 20), height=3, width=6, bg="Azure", command=lambda: on_click(btn1))
    btn2 = Button(root, text=" ", font=("Gill Sans", 20), height=3, width=6, bg="Azure", command=lambda: on_click(btn2))
    btn3 = Button(root, text=" ", font=("Gill Sans", 20), height=3, width=6, bg="Azure", command=lambda: on_click(btn3))
    
    btn4 = Button(root, text=" ", font=("Gill Sans", 20), height=3, width=6, bg="Azure", command=lambda: on_click(btn4))
    btn5 = Button(root, text=" ", font=("Gill Sans", 20), height=3, width=6, bg="Azure", command=lambda: on_click(btn5))
    btn6 = Button(root, text=" ", font=("Gill Sans", 20), height=3, width=6, bg="Azure", command=lambda: on_click(btn6))
    
    btn7 = Button(root, text=" ", font=("Gill Sans", 20), height=3, width=6, bg="Azure", command=lambda: on_click(btn7))
    btn8 = Button(root, text=" ", font=("Gill Sans", 20), height=3, width=6, bg="Azure", command=lambda: on_click(btn8))
    btn9 = Button(root, text=" ", font=("Gill Sans", 20), height=3, width=6, bg="Azure", command=lambda: on_click(btn9))
    
    	
    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=0, column=2)
    
    btn4.grid(row=1, column=0)
    btn5.grid(row=1, column=1)
    btn6.grid(row=1, column=2)
    
    btn7.grid(row=2, column=0)
    btn8.grid(row=2, column=1)
    btn9.grid(row=2, column=2)


def disable_btns():
	btn1.config(state=DISABLED)
	btn2.config(state=DISABLED)
	btn3.config(state=DISABLED)
	btn4.config(state=DISABLED)
	btn5.config(state=DISABLED)
	btn6.config(state=DISABLED)
	btn7.config(state=DISABLED)
	btn8.config(state=DISABLED)
	btn9.config(state=DISABLED)


def won():
	global win
	win = False

	if btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"]  == "X":
		btn1.config(bg="cyan")
		btn2.config(bg="cyan")
		btn3.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  X Wins!!")
		disable_btns()
	elif btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"]  == "X":
		btn4.config(bg="cyan")
		btn5.config(bg="cyan")
		btn6.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  X Wins!!")
		disable_btns()

	elif btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"]  == "X":
		btn7.config(bg="cyan")
		btn8.config(bg="cyan")
		btn9.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  X Wins!!")
		disable_btns()

	elif btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"]  == "X":
		btn1.config(bg="cyan")
		btn4.config(bg="cyan")
		btn7.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  X Wins!!")
		disable_btns()

	elif btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"]  == "X":
		btn2.config(bg="cyan")
		btn5.config(bg="cyan")
		btn8.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  X Wins!!")
		disable_btns()

	elif btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"]  == "X":
		btn3.config(bg="cyan")
		btn6.config(bg="cyan")
		btn9.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  X Wins!!")
		disable_btns()

	elif btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"]  == "X":
		btn1.config(bg="cyan")
		btn5.config(bg="cyan")
		btn9.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  X Wins!!")
		disable_btns()

	elif btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"]  == "X":
		btn3.config(bg="cyan")
		btn5.config(bg="cyan")
		btn7.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  X Wins!!")
		disable_btns()

	elif btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"]  == "O":
		btn1.config(bg="cyan")
		btn2.config(bg="cyan")
		btn3.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  O Wins!!")
		disable_btns()
        
	elif btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"]  == "O":
		btn4.config(bg="cyan")
		btn5.config(bg="cyan")
		btn6.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  O Wins!!")
		disable_btns()

	elif btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"]  == "O":
		btn7.config(bg="cyan")
		btn8.config(bg="cyan")
		btn9.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  O Wins!!")
		disable_btns()

	elif btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"]  == "O":
		btn1.config(bg="cyan")
		btn4.config(bg="cyan")
		btn7.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  O Wins!!")
		disable_btns()

	elif btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"]  == "O":
		btn2.config(bg="cyan")
		btn5.config(bg="cyan")
		btn8.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  O Wins!!")
		disable_btns()

	elif btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"]  == "O":
		btn3.config(bg="cyan")
		btn6.config(bg="cyan")
		btn9.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  O Wins!!")
		disable_btns()

	elif btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"]  == "O":
		btn1.config(bg="cyan")
		btn5.config(bg="cyan")
		btn9.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  O Wins!!")
		disable_btns()

	elif btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"]  == "O":
		btn3.config(bg="cyan")
		btn5.config(bg="cyan")
		btn7.config(bg="cyan")
		win = True
		messagebox.showinfo("3-in-a-Row", "CONGRATULATIONS!  O Wins!!")
		disable_btns()

	if count == 9 and win == False:
		messagebox.showinfo("3-in-a-Row", "It's A Tie!\n No One Wins!")
		disable_btns()

def on_click(btn):
	global clicked, count

	if btn["text"] == " " and clicked == True:
		btn["text"] = "X"
		clicked = False
		count += 1
		won()
	elif btn["text"] == " " and clicked == False:
		btn["text"] = "O"
		clicked = True
		count += 1
		won()
	else:
		messagebox.showerror("3-in-a-Row", "Hey! That box has already been selected\nPick Another Box..." )

my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="New Game", command=newgame)
newgame()


root.mainloop()
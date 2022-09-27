import pyautogui
import time
from tkinter import *

root = Tk()
root.geometry("600x500")
key_map = {
    "R": "I",
    "R'": "K",
  
    "U": "J",
    "U'": "F",

    "F": "H",
    "F'": "G",

    "D": "S",
    "D'": "L",

    "B": "W",
    "B'": "O",

    "L": "D",
    "L'": "E"


}



def reverse_scramble(s):
    a = s.split(" ")
    for i in range(len(a)):
        if a[i][-1] == "'":
            a[i] = a[i][:-1]
        elif a[i].endswith("2"):
            continue
        else:
            a[i]=a[i] + "'"
    a.reverse()

    return a

def solve_cube(solution):
    time.sleep(2)
    pyautogui.press(" ", presses=2)
    for i in solution:
        if i.endswith("2"):
            pyautogui.press(key_map[i[:-1]], presses=2)
        else:
            pyautogui.press(key_map[i])

def main(text_widget):
    s = text_widget.get()
    solve_cube(reverse_scramble(s))
    text_widget.delete(0, END)


scramble = Entry(root, text="Enter the scramble: ", width=75,font=('Roboto'), justify=CENTER)
scramble.pack()
solve = Button(root,text = "Run",font=('Roboto'), command = lambda:main(scramble))
solve.pack()
root.mainloop()





#Gui Click and Collect
#Natalie, May, 2020

from tkinter import *
import tkinter as tk



def main_screen():
    global screen
    screen = tk.Tk()
    screen.title("Click and Collect")
    screen.geometry("600x600")

    Label(text = "Welcome to BDSC Click and Collect!", font = ("Arial", "24", "bold")).pack()
    Label(text = "Wowie", font = ("Arial", "20")).pack()
    
    screen.mainloop()
main_screen()
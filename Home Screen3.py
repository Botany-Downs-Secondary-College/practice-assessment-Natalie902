#home Screen for S.T.A.R.S with Banner
#Natalie, March

from tkinter import*

def Screen1():
    global frame1
    global frame2
    
    frame2.grid_remove()
   
   
    Title = Label(bg = "black", height = "500", width = "500", borderwidth = 0, highlightthickness = 0)
    Title.grid(row = 10, column = 1)
    
    photo = PhotoImage(file = "Title3.gif")
    label = Label(Title, image = photo,borderwidth = 0, highlightthickness = 0)
    label.image = photo
    label.grid(row = 1, column = 1)
    
    optionbox = Label(bg = "black", fg = "white", height = "500", width = "500")
    optionbox.grid(row = 13, column = 1) 
    
    startbutton = Button(optionbox, text = "Start Game", anchor = W, command = Screen2, bg = "black", fg = "white", padx = 10, pady = 10)
    startbutton.grid(row = 8, column = 1)
    
    exitbutton = Button(optionbox, text = "Quit Game", anchor = W, command = root.destroy, bg = "black", fg = "white", padx = 10, pady = 10)
    exitbutton.grid(row = 9, column = 1)
    
def Screen2():
    global frame1
    global frame2
    frame1.grid_remove()

    import Space_Invaders_15
    
#Main Routine

root = Tk()
root.title("Home")
root.configure(background = "black")
root.geometry("600x600+350+50")
frame1 = Frame(root)
frame2 = Frame(root)

Screen1()
root.mainloop()
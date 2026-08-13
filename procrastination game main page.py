import tkinter as tk
from tkinter import ttk

page_open = 0

#homework command

def homework():
    global page_open
    if page_open == 0:
        homework_window = tk.Tk()
        homework_window.geometry ('300x150')
        homework_window.title("homework")
        page_open += 1
        window.withdraw()
    else:
        pass
        


#minigame command
def minigame():
    global page_open
    if page_open == 0:
        minigame_window = tk.Tk()
        minigame_window.geometry('300x150')
        minigame_window.title("minigame!")
        page_open += 1
        window.withdraw()
    
    else:
        pass

#minigame 1


window = tk.Tk()
window.geometry('300x150')
window.title("An Assingment")

#title
title = ttk.Label(master = window, text = "would you like to:")
title.pack()

#area where buttons should be
button_area = ttk.Frame(master=window)
button_area.pack()

#making the homework button
homework_button = ttk.Button(master = button_area, text = "homework", command = homework)
homework_button.pack(side = 'left', padx= '20', pady = '30')

#making the minigame button
minigame_button = ttk.Button(master = button_area, text = "minigame!", command = minigame)
minigame_button.pack(side = 'left', padx= '20', pady = '30')

root.protocol("WM")

#run the window
window.mainloop()

import tkinter as tk
from tkinter import ttk

#homework command



#making the window
window = tk.Tk()
window.geometry ('300x150')
window.title("An Assingment")

#title
title = ttk.Label(master = window, text = "would you like to:")
title.pack()

#area where buttons should be
button_area = ttk.Frame(master=window)
button_area.pack()

#making the homework button
homework_button = ttk.Button(master = button_area, text = "homework")
homework_button.pack(side = 'left', padx= '20', pady = '30')

#making the minigame button
minigame_button = ttk.Button(master = button_area, text = "minigame!")
minigame_button.pack(side = 'left', padx= '20', pady = '30')

#run the window
window.mainloop()
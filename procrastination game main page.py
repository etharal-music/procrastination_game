import tkinter as tk
from tkinter import ttk



############
#this is the time function allowing me to make the code wait
import time
############



page_open = 0

###########
#this is the percentage of the homework being done
homework_done = 0
###########


#homework command

def homework():
    global homework_done
    global page_open
    if page_open == 0:
        print("cheese")
        homework_window = tk.Tk()
        homework_window.geometry ('300x150')
        homework_window.title("homework")
        page_open += 1
        window.withdraw()
        print('cheese')
        #homework progress bar
        Progress_bar = ttk.Progressbar( master = homework_window, length = 200)
        print('cheese')
        Progress_bar["value"] = 0
        Progress_bar.pack(pady = 20)
        current_value = Progress_bar['value']
        def load_bar():
            print(current_value)
            if Progress_bar['value'] < 100:
                Progress_bar['value'] += 1

                homework_window.after(50, load_bar)
            else:
                homework_window.withdraw()
                window.deiconify()
                page_open -= 1
        load_bar()


        
    

    else:
        pass
        


#minigame command
def minigame():
    global page_open
    if page_open == 0:
        minigame_1_window = tk.Tk()
        minigame_1_window.geometry('300x150')
        minigame_1_window.title("minigame!")
        page_open += 1
        window.withdraw()
    
    else:
        pass

#minigame 1


#window
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



#run the window
window.mainloop()

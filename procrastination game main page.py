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
        homework_window = tk.Tk()
        homework_window.geometry ('300x150')
        homework_window.title("homework")
        page_open += 1
        window.withdraw()
        #homework progress bar
        Progress_bar = ttk.Progressbar( master = homework_window, length = 200)
        Progress_bar["value"] = 0
        Progress_bar.pack(pady = 20)
        def load_bar():
            global homework_done
            global page_open
            print(Progress_bar['value'])
            if Progress_bar['value'] < 100:
                Progress_bar['value'] += 1

                homework_window.after(9000, load_bar)
            else:
                homework_done += 10
                page_open -= 1
                homework_window.withdraw()
                window.deiconify()

        load_bar()


        
    

    else:
        pass
        


#minigame command
def minigame():
    global page_open
    if page_open == 0:
        #first minigame!
        minigame_1_window = tk.Tk()
        minigame_1_window.geometry('300x150')
        minigame_1_window.title("minigame!")
        minigame_1_done = False
        checkboxes_clicked = 0
        page_open += 1
        window.withdraw()
        tickbox_bar = tk.BooleanVar()
        tickbox_bar2= tk.BooleanVar()
        tickbox_bar3= tk.BooleanVar()
        tickbox_bar4= tk.BooleanVar()
        tickbox_bar5= tk.BooleanVar()
        tickbox_bar6= tk.BooleanVar()
        tickbox_bar7= tk.BooleanVar()
        tickbox_bar8= tk.BooleanVar()
        tickbox_bar9= tk.BooleanVar()
        tickbox_bar10= tk.BooleanVar()
        tickbox_bar11= tk.BooleanVar()
        tickbox_bar12= tk.BooleanVar()

        #minigame 1 is a bunck of check boxes you have to check
        minigame_label = ttk.Label(master= minigame_1_window, text= "tick all the boxes!")
        minigame_label.pack()
        checkbox_1 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar)
        checkbox_1.pack()
        checkbox_2 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar2)
        checkbox_2.pack(side = 'left')
        checkbox_3 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar3)
        checkbox_3.pack(side = 'right')
        checkbox_4 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar4)
        checkbox_4.pack()
        checkbox_5 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar5)
        checkbox_5.pack(side= 'left')
        checkbox_6 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar6)
        checkbox_6.pack(side = 'right')
        checkbox_7 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar7)
        checkbox_7.pack()
        checkbox_8 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar8)
        checkbox_8.pack(side = 'left')
        checkbox_9 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar9)
        checkbox_9.pack(side = 'right')
        checkbox_10 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar10)
        checkbox_10.pack()
        checkbox_11 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar11)
        checkbox_11.pack(side = 'left')
        checkbox_12 = ttk.Checkbutton(master = minigame_1_window, variable = tickbox_bar12)
        checkbox_12.pack(side = 'right')

        while minigame_1_done == False:
            if tickbox_bar == True:
                checkboxes_clicked +=1
                print(checkboxes_clicked)

    
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

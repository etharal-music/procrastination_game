import tkinter as tk
from tkinter import ttk



############
#this is the time function allowing me to make the code wait
import time
############


###########
#this variable checks if a page is open, if so it will add one and stop any other page from
#being opened
page_open = 0
###########

###########
#this is the percentage of the homework being done
homework_done = 0
###########

time_until_homework = 72

#homework command

def homework():
    global homework_done
    global page_open
    global time_until_homework
    #this check if there is another page open, if so it does not allow another to open
    if page_open == 0:
        homework_window = tk.Tk()
        homework_window.geometry ('300x150')
        homework_window.title("homework")
        page_open += 1
        #deletes the main window for now
        window.withdraw()
        #homework progress bar
        Progress_bar = ttk.Progressbar( master = homework_window, length = 200)
        Progress_bar["value"] = 0
        Progress_bar.pack(pady = 20)
        def load_bar():
            global homework_done
            global page_open
            global time_until_homework
            print(Progress_bar['value'])
            #if the progres bar is not complete: add one to it and wait a second
            if Progress_bar['value'] < 100:
                Progress_bar['value'] += 1

                homework_window.after(50, load_bar)
            else:
            #if the progress bar is complete, take away 6 hours from the ingame clock, allow page acess,
            #respawn main window aswell as delete this one and make the homework 10 % done
                homework_done += 10
                page_open -= 1
                time_until_homework -= 6
                homework_window.withdraw()
                window.deiconify()
                thing()
                
        load_bar()

    else:
        pass
        

#minigame command
def minigame():
    global time_until_homework
    global page_open
    global minigame_1_done
    global checkboxes_clicked

    my_booleans = []
    my_checkboxes = []

    def my_checkbox_clicked(i):
        global minigame_1_done
        global checkboxes_clicked
        checkboxes_clicked = 0
        if my_booleans[i] == True:
            print("true")
        else:
            print("false")

    if page_open == 0:
        #first minigame!
        minigame_1_window = tk.Tk()
        minigame_1_window.geometry('300x150')
        minigame_1_window.title("minigame!")
        minigame_1_done = False
        checkboxes_clicked = 0
        page_open += 1
        window.withdraw()

        for i in range(12):
            my_booleans.append(tk.BooleanVar)


        #minigame 1 is a bunck of check boxes you have to check
        minigame_label = ttk.Label(master= minigame_1_window, text= "tick all the boxes!")
        minigame_label.pack()

        pack_side = 0

        for i in range(12):
            my_checkbox = ttk.Checkbutton(master = minigame_1_window, variable = my_booleans[i], command = lambda i=i: my_checkbox_clicked(i)
)
            if pack_side == 0:
                my_checkbox.pack()
                pack_side += 1
            elif pack_side == 1:
                my_checkbox.pack(side = 'left')
                pack_side += 1
            else:
                my_checkbox.pack(side = 'right')
                pack_side = 0
            my_checkboxes.append(my_checkbox)

    
    else:
        pass

#minigame 1


#window
window = tk.Tk()
window.geometry('300x150')
window.title("An Assingment")


#label to tell the user how long until the homework is due
time_until_homework_label = ttk.Label(master = window, text = "")
time_until_homework_label.pack()

def thing():
    time_until_homework_label["text"] = time_until_homework
thing()


#title
title = ttk.Label(master = window, text = "would you like to:")
title.pack()


#area where buttons should be
button_area = ttk.Frame(master=window)
button_area.pack()

#the homework button
homework_button = ttk.Button(master = button_area, text = "homework", command = homework)
homework_button.pack(side = 'left', padx= '20', pady = '30')

#the minigame button
minigame_button = ttk.Button(master = button_area, text = "minigame!", command = minigame)
minigame_button.pack(side = 'left', padx= '20', pady = '30')



#run the window
window.mainloop()

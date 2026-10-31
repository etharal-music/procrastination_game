import tkinter as tk
from tkinter import ttk


timer_minigame_1_label = 0


minigame_2_done = False

minigame_choice = ""

############
#this is the time function allowing me to make the code wait
import time
############

############
# this is a random function allowing me to randomize minigames.
import random
############

minigame_1_time_left = 10

############
# this is a variable that changes the homework buttons size
homework_button_width = 11
############

############
# a variable decideing how long homework takes
load_time = 200
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

time_until_homework = 84


#homework command

def homework():
    global homework_done
    global page_open
    global load_time
    global time_until_homework
    #this check if there is another page open, if so it does not allow another to open
    if page_open == 0:
        homework_window = tk.Toplevel()
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
            global load_time
            global time_until_homework
            print(Progress_bar['value'])
            #if the progres bar is not complete: add one to it and wait a second
            if Progress_bar['value'] < 100:
                Progress_bar['value'] += 1

                homework_window.after(load_time, load_bar)
            else:
            #if the progress bar is complete, take away 6 hours from the ingame clock, allow page acess,
            #respawn main window aswell as delete this one and make the homework 10 % done
                homework_done += 10
                page_open -= 1
                time_until_homework -= 6
                homework_window.withdraw()
                window.deiconify()
                load_time -= 30
                update_time()
                homework_left()
                if homework_done >= 100:
                    ending()
                elif time_until_homework <= 0:
                    ending()
                else:
                    pass
                
        load_bar()

    else:
        pass
        

#minigame command
def minigame():
    global time_until_homework
    global homework_done
    global page_open
    global minigame_1_done
    global checkboxes_clicked
    global minigame_choice
    global minigame_1_time_left

    my_booleans = []
    my_checkboxes = []
    if page_open == 0:
        def my_checkbox_clicked(i):
            global homework_button_width
            global minigame_1_done
            global checkboxes_clicked
            global page_open
            global time_until_homework
            global minigame_reroll
            global minigame_1_time_left

            if my_booleans[i].get() == True:
                checkboxes_clicked += 1
            else: 
                checkboxes_clicked -= 1
            print(checkboxes_clicked)

            


            if checkboxes_clicked != 12 and minigame_1_time_left != 0:
                print("hi")
                pass            
            else:
                minigame_1_ending()

        def minigame_1_ending():
            global page_open
            global time_until_homework
            print("bye")
            minigame_1_done == True
            page_open -= 1
            time_until_homework -= 6
            minigame_1_window.withdraw()
            window.deiconify()
            minigame_reroll()
            homework_button_size()
            update_time()
            if time_until_homework <= 0:
                ending()

        #timer functions
        def start_minigame_1_timer():
            print ("starting timer")
            window.after(1000, countdown_minigame_1_timer)

        def countdown_minigame_1_timer():
            global timer_minigame_1_label
            global minigame_1_time_left
            if minigame_1_time_left > 0:
                minigame_1_time_left -= 1
                print (minigame_1_time_left)
                window.after(1000, countdown_minigame_1_timer)
                timer_minigame_1_label["text"] = str(minigame_1_time_left)
            else:
                minigame_1_ending()

        def checkbox_toggle(i):
            global checkboxes_clicked
            if my_booleans[i].get() == False:
                my_booleans[i].set(True)
                checkboxes_clicked += 1
                print("x")
                print(checkboxes_clicked)
                print("x")
            else:
                my_booleans[i].set(False)
                checkboxes_clicked -= 1

        def checkbox_randomizer(i):
            global checkboxes_clicked
            global homework_button_width
            global page_open
            global homework_button_width
            global time_until_homework
            global window
            global minigame_2_done
            global minigame_reroll
            if i == 1:
                checkbox_toggle(5)
                checkbox_toggle(10)
            print(i)
            if i == 2:
                checkbox_toggle(6)
                checkbox_toggle(10)
            if i == 3:
                checkbox_toggle(8)
                checkbox_toggle(2)
            if i == 4:
                checkbox_toggle(11)
                checkbox_toggle(7)
            if i == 5:
                checkbox_toggle(0)
            if i == 6:
                checkbox_toggle(1)
                checkbox_toggle(9)
            if i == 7:
                checkbox_toggle(2)
            if i == 8:
                checkbox_toggle(0)
                checkbox_toggle(3)
            if i == 9:
                checkbox_toggle(4)
                checkbox_toggle(11)
            if i == 10:
                checkbox_toggle(7)
            if i == 11:
                checkbox_toggle(4)
                checkbox_toggle(7)

            if my_booleans[i].get() == True:
                checkboxes_clicked += 1
            else:
                checkboxes_clicked -= 1
            print(checkboxes_clicked)
        

            if checkboxes_clicked != 12:
                        print("hi")
                        pass
                    
            else:
                print("bye")
                minigame_2_done == True
                page_open -= 1
                time_until_homework -= 6
                minigame_2_window.withdraw()
                window.deiconify()
                minigame_reroll()
                homework_button_width -= 3
                update_time()
                if time_until_homework <= 0:
                    ending()

    

        if minigame_choice == 1:
            #first minigame!
            minigame_1_window = tk.Toplevel()
            minigame_1_window.geometry('300x150')
            minigame_1_window.title("minigame!")
            minigame_1_done = False
            checkboxes_clicked = 0
            page_open += 1
            window.withdraw()
            

            for i in range(12):
                my_booleans.append(tk.BooleanVar())


            #minigame 1 is a bunck of check boxes you have to check
            minigame_label = ttk.Label(master= minigame_1_window, text= "tick all the boxes!")
            minigame_label.pack()

            timer_minigame_1_label = ttk.Label(master = minigame_1_window, text = 10)
            timer_minigame_1_label.pack()

            pack_side = 0

            for i in range(12):
                my_checkbox = ttk.Checkbutton(master = minigame_1_window, variable = my_booleans[i], command = lambda i=i: my_checkbox_clicked(i))
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

            start_minigame_1_timer()
          

        
        


        if minigame_choice == 2:
        #second minigame!
            minigame_2_window = tk.Toplevel()
            minigame_2_window.geometry('300x150')
            minigame_2_window.title("minigame!")
            minigame_2_done = False
            checkboxes_clicked = 0
            page_open += 1
            window.withdraw()
            

            for i in range(12):
                my_booleans.append(tk.BooleanVar())


            #minigame 1 is a bunck of check boxes you have to check
            minigame_label_2 = ttk.Label(master= minigame_2_window, text= """tick all the boxes!
            (good luck)""")
            minigame_label_2.pack()

            pack_side = 0

            for i in range(12):
                my_checkbox = ttk.Checkbutton(master = minigame_2_window, variable = my_booleans[i], command = lambda i=i: checkbox_randomizer(i))
                if pack_side == 0:
                    my_checkbox.pack(side = 'left')
                    pack_side += 1
                else:
                    my_checkbox.pack(side = 'right')
                    pack_side = 0
                my_checkboxes.append(my_checkbox)
        
        else:
            pass


def minigame_reroll():
    global minigame_choice
    minigame_choice = random.choice([1,2])
    print (minigame_choice)
minigame_reroll()






#window
window = tk.Tk()
window.geometry('300x150')
window.title("An Assingment")

time_until_homework_label_label = ttk.Label(master = window, text = "hours until homework due:")
time_until_homework_label_label.pack()

#label to tell the user how long until the homework is due
time_until_homework_label = ttk.Label(master = window, text = "")
time_until_homework_label.pack()


homework_percentage_label = ttk.Label(master = window, text = "percentage of homework done:")
homework_percentage_label.pack()

#label to say how much of the homework is complete
homework_percentage = ttk.Label(master = window, text = "")
homework_percentage.pack()

def update_time():
    time_until_homework_label["text"] = time_until_homework
update_time()

def homework_left():
    homework_percentage["text"] = homework_done
homework_left()   

#title
title = ttk.Label(master = window, text = "would you like to:")
title.pack()


#area where buttons should be
button_area = ttk.Frame(master=window)
button_area.pack()

#the homework button
homework_button = ttk.Button(master = button_area, text = "homework", command = homework, width = homework_button_width)
homework_button.pack(side = 'left', padx= '20')

def homework_button_size():
    homework_button["width"] -= 1
homework_button_size()


#the minigame button
minigame_button = ttk.Button(master = button_area, text = "minigame!", command = minigame)
minigame_button.pack(side = 'left', padx= '20' )

def ending():
    global window
    global minigame_1_done
    global checkboxes_clicked
    global page_open
    global time_until_homework
    print("end")
    end_window = tk.Toplevel()
    end_window.geometry('300x150')
    end_window.title("ending")
    page_open += 1
    window.withdraw()

    if homework_done == 100 and time_until_homework >= 0 and time_until_homework <= 23:
        print('''nuetral you got the nuetal ending
you handed in your homework, but just in time.
you may close the game''')
        nuetral_title = ttk.Label(text = "neutral", master = end_window)
        nuetral_title.pack()
    elif homework_done == 100 and time_until_homework == 24:
        print('good')
        good_title = ttk.Label(text = """you got the good ending
good job you did everything you where meant to!
you may close the game when you please""", master = end_window)
        good_title.pack()
    else:
        bad_title = ttk.Label(text = """you got the bad ending
Im very dissapointed
close the game.""", master = end_window)
        bad_title.pack()
        print("bad")
        
    pass

#run the window
window.mainloop()
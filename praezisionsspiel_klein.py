import tkinter as tk
from tkinter import *
from random import randint
#erstellung des Fensters für das Spiel
spiel  = tk.Tk()
spiel.config(bg='navy blue')
#fullscreen
w, h = spiel.winfo_screenwidth(), spiel.winfo_screenheight()        
spiel.overrideredirect(1)
spiel.geometry('%dx%d+0+0' %(w, h))
#erstellung eines Labels das die Zeit abzeigt
timer = tk.Label(spiel,text=10)
timer.pack(anchor='center')
#zeitvariable wird ein wert zugewiesen
time_left = 31
#funktion die das Label updatet und alle 1000 ms die zeit - 1 rechnet
def countdown():
    global time_left 
    time_left -= 1
    if time_left >= 0:
        timer.config(text=str(time_left))
        spiel.after(1000,countdown)
    else:
        spiel.destroy()
countdown()
#die treffer mit der count variable = 0 setzen
count = 0
#funkion die +1 rechnet bei jedem Treffer
def counter(a): 
    global count 
    count += a
    hit_label.config(text=("Aktuelle Punktzahl:",count))
    hit_label.update()
#label das Treffer anzeigt
hit_label = tk.Label(spiel,text=("Aktuelle Punktzahl:",0))
hit_label.place(x=0,y=0)
#funtion die das Target verschiebt
def move_target():
    target.place(x=randint(0, 1360), y=randint(0, 520))
    counter(1)
#button der als Zielscheibe dient
target = tk.Button(spiel, width=2, height=1, bg="red",command=move_target)
target.place(x=randint(0, 1360), y=randint(0, 520))
#button der das spiel frühzeitig beendet
quit_button = tk.Button(text='Schießen',master=spiel,font=('Arial', 18),command=spiel.destroy,bg='dark grey')
quit_button.place(x=0,y=h-47)
spiel.mainloop()
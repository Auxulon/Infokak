import tkinter as tk

spiel = tk.Tk()
spiel.geometry('500x500')

timer = tk.Label(spiel,text=10)
timer.pack(anchor='center')
 
time_left =11

def countdown():
    global time_left 
    time_left -= 1
    if time_left >= 0:
        timer.config(text=str(time_left))
        spiel.after(1000,countdown)
    else:
        spiel.destroy()
countdown()

spiel.mainloop()
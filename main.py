#importieren von tkinter und randit zum arbeiten
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
#erstellen des Hauptmenüs als tkinter-klasse mit der Überschrift Hauptmenu
def open_menu():
    menu = Tk()
    menu.geometry('1920x1080')
    menu.config(bg='gray')
    label = tk.Label(menu,text='Hauptmenu',font=('Arial' , 20),bg='dark grey')
    label.pack()
    #eine Funktion die im Dropdownmenu agiert und die spielmodi und Schwierigkeiten startet
    def dropdownmenu_zt(laenge):
        if zeitwahl.get() == 'Kurz(10s)':
            import zeitspiel_kurz 
        elif zeitwahl.get() == 'Mittel(30s)':
            import zeitspiel_mittel
        else :
            import zeitspiel_lang
            
        menu.destroy()
    #eine liste mit werten die gewählt werden können
    ztauswahl = ['Kurz(10s)','Mittel(30s)','Lang(60s)']
    #einrichtung einer Wahlvariable
    zeitwahl = StringVar()
    zeitwahl.set(ztauswahl[1])
    #erstellung des menüs mit dem OptionMenu modul
    ztdrop = OptionMenu(menu,zeitwahl,*ztauswahl,command=dropdownmenu_zt)
    ztdrop.config(bg='dark grey',fg='black')
    aufzeit = tk.Label(text='Auf Zeit',bg='grey',font=('Arial',16))
    #verpacken damit sie auf dem Hauptmenü erscheinen
    aufzeit.pack()
    ztdrop.pack()
    #eine Funktion die im Dropdownmenu agiert und die spielmodi und Schwierigkeiten startet
    def dropdownmenu_pz(größe):
        if praezision.get() == 'Kleine Ziele':
            import praezisionsspiel_klein
        elif praezision.get() == 'Mittlere Ziele':
            import praezisionsspiel_mittel
        else:
            import praezisionsspiel_groß
        
        menu.destroy()
    #eine liste mit werten die gewählt werden können
    pzauswahl = ['Kleine Ziele','Mittlere Ziele','Große Ziele']
    #einrichtung einer Wahlvariable
    praezision = StringVar()
    praezision.set(pzauswahl[1])
    #erstellung des menüs mit dem OptionMenu modul
    pzdrop = OptionMenu(menu,praezision,*pzauswahl,command=dropdownmenu_pz)
    pzdrop.config(bg='dark grey',fg='black')
    aufpraezision = tk.Label(text='Auf Präzision',bg='grey',font=('Arial',16))
    #verpacken damit sie auf dem Hauptmenü erscheinen
    aufpraezision.pack()
    pzdrop.pack()
    #Verschiedene Buttons und Lables werden auf menu erstellt um die definierten Funktionen anzuwenden
    quit_button = tk.Button(text='Schießen',master=menu,font=('Arial', 18),command=menu.destroy,bg='dark grey')
    quit_button.place(x=0,y=790)
    
    menu.mainloop()
open_menu()
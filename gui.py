from tkinter import *
from tkinter import ttk
import subject3 as s
import classmark1 as c
import location as l




class Library:
    def __init__(self,window):
        self.master = window
        self.master.title("Keele Library Map")
        self.width=self.master.winfo_screenwidth()
        self.height=self.master.winfo_screenheight()
        self.master.geometry(f"{self.width}x{self.height}+0+0")
        self.master.state('zoomed')
        # Creating top Frame with Label
        self.topFrame=Frame(self.master,bg='#1b9ea4', height=200)
        self.topFrame.pack(fill=X)
        self.klm=Label(self.topFrame,text='Keele Library Map',bg='#1b9ea4',fg='white', font=('tahona', 50), pady=100)
        self.klm.pack()
        # Creating center Frame
        self.centerFrame=Frame(self.master,height=200)
        self.centerFrame.pack(fill=X)

        # Creating subject Frame
        openSubject = s.Subject(self.centerFrame)

        # Creating classmark Frame
        openClassmark = c.Classmark(self.centerFrame)

        # Creating location Frame
        openLocation = l.Location(self.centerFrame)


        # Center Labels with the screen width
        self.centerFrame.grid_columnconfigure(0, weight=1)
        self.centerFrame.grid_columnconfigure(1, weight=1)
        self.centerFrame.grid_columnconfigure(2, weight=1)

if __name__ == '__main__':
    window = Tk()
    print(window.winfo_screenwidth())
    print(window.winfo_screenheight())
    std = Library(window)
    mainloop()       




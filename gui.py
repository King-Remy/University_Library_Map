'''
FIlename: 
AUthor: King Remy Igbokwe
Student ID: 21027699
Date: 17/12/2022

Keele University Library app that displays the following stored information:
Subject, Classmark, Location

User can select any subject, classmark or location in the Library and it would display the related search via the library app GUI.
'''

from tkinter import *
import subject3 as s
import classmark1 as c
import location as l

class Library:
    def __init__(self,window):          # Method sets the properties for the Library window 
        self.master = window
        self.master.title("Keele Library Map")
        self.master.iconbitmap('Keele-logo2.ico')       # Change the window icon to Keele University logo
        self.width=self.master.winfo_screenwidth()          # Gets the width of window screen
        self.height=self.master.winfo_screenheight()            # Gets the height of window screen
        self.master.geometry(f"{self.width}x{self.height}+0+0")         # Set width and heigh geometry of window
        self.master.state('zoomed')             # Ensures window is fully fit to the edges of screen
        
        # Creating top Frame with Label
        self.topFrame=Frame(self.master,bg='#281F3E', height=200)
        self.topFrame.pack(fill=X)
        self.klm=Label(self.topFrame,text='Keele Library Map',bg='#281F3E',fg='white', font=('tahona', 50), pady=100)
        self.klm.pack()

        # Adding Keele university logo at top right of right frame
        self.imageLogo = PhotoImage(file='Keele logo.png')

        self.labelLogo = Label(self.topFrame, image=self.imageLogo)            # Label created on right frame for  keele logo iamge
        self.labelLogo.place(x=1300, y= 20)

        # Creating center Frame
        self.centerFrame=Frame(self.master)
        self.centerFrame.pack(fill=BOTH)

        self.image = PhotoImage(file='Library2.png')

        self.imglabel = Label(self.centerFrame, image=self.image)
        self.imglabel.pack(fill=BOTH)
        

        # Creating subject logo selection and selected window
        openSubject = s.Subject(self.centerFrame)

        # Creating classmark logo selection and selected window
        openClassmark = c.Classmark(self.centerFrame)

        # Creating location logo selection and selected window
        openLocation = l.Location(self.centerFrame)

        # Placing each subject, classmark and location logo selection in center frame with equal spacing
        # self.centerFrame.grid_columnconfigure(0, weight=1)
        # self.centerFrame.grid_columnconfigure(1, weight=1)
        # self.centerFrame.grid_columnconfigure(2, weight=1)

if __name__ == '__main__':          # Prevents invoking the script when not ran
    window = Tk()
    print(window.winfo_screenwidth())
    print(window.winfo_screenheight())
    std = Library(window)
    mainloop()       
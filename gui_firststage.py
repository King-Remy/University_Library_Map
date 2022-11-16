from tkinter import *
from tkinter import ttk





class Student:
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
        self.subject=Frame(self.centerFrame,pady=100,padx=100)
        self.subject.grid(row=0,column=0,sticky='senw')
        self.img=PhotoImage(file='subject_logo4.png')
        self.imgSubject=Label(self.subject,image=self.img,padx=10,pady=10)
        self.imgSubject.pack()
        self.buttonSubject = Button(self.subject, text='Subject Name', bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonSubject.pack()

        # Creating classmark Frame
        self.classmark=Frame(self.centerFrame,pady=100,padx=100)
        self.classmark.grid(row=0,column=1,sticky='senw')
        self.img2=PhotoImage(file='classmark_logo4.png')
        self.imgClassmark=Label(self.classmark,image=self.img2,padx=10,pady=10)
        self.imgClassmark.pack()
        self.buttonClassmark = Button(self.classmark, text='Class Mark', bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonClassmark.pack()

        # Creating location Frame
        self.location=Frame(self.centerFrame,pady=100,padx=100)
        self.location.grid(row=0,column=2,sticky='senw')
        self.img3=PhotoImage(file='location_logo1.png')
        self.imgLocation=Label(self.location,image=self.img3,padx=10,pady=10)
        self.imgLocation.pack()
        self.buttonClassmark = Button(self.location, text='Location', bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonClassmark.pack()
        # Center Labels with the screen width
        self.centerFrame.grid_columnconfigure(0, weight=1)
        self.centerFrame.grid_columnconfigure(1, weight=1)
        self.centerFrame.grid_columnconfigure(2, weight=1)



if __name__ == '__main__':
    window = Tk()
    # print(window.winfo_screenwidth())
    # print(window.winfo_screenheight())
    std = Student(window)
    mainloop()       




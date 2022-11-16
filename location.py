from tkinter import *

class Location:
    def __init__(self, cf):
        # Creating location Frame
        self.location=Frame(cf,pady=100,padx=100)
        self.location.grid(row=0,column=2,sticky='senw')
        self.img3=PhotoImage(file='location_logo1.png')
        self.imgLocation=Label(self.location,image=self.img3,padx=10,pady=10)
        self.imgLocation.pack()
        self.buttonClassmark = Button(self.location, command=self.openlocationwindow, text='Location', bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonClassmark.pack()


    def openlocationwindow(self):
        self.master = Toplevel()
        self.master.title('Location')
        self.master.geometry("800x600+150+150")
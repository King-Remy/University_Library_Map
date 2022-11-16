from tkinter import *
from tkinter import ttk
from prof import *
from gui import *

class Classmark:
    def __init__(self,centerFrame):
        # Creating classmark Frame
        self.classmark=Frame(centerFrame,pady=100,padx=100)
        self.classmark.grid(row=0,column=1,sticky='senw')
        self.img2=PhotoImage(file='classmark_logo4.png')
        self.imgClassmark=Label(self.classmark,image=self.img2,padx=10,pady=10)
        self.imgClassmark.pack()
        self.buttonClassmark = Button(self.classmark, command=self.openclassmarkwindow, text='Classmark', bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonClassmark.pack()

    def openclassmarkwindow(self):
        self.master = Toplevel()
        self.master.title('Classmark')
        self.width=self.master.winfo_screenwidth()
        self.height=self.master.winfo_screenheight()
        self.master.geometry(f"{self.width}x{self.height}+0+0")
        self.master.state('zoomed')
        # Creating Left frame for new opened window
        self.frameLeft=Frame(self.master,bg='red',width=512)
        self.frameLeft.pack(side=LEFT,fill=BOTH)

        self.frameRight=Frame(self.master,bg='green',width=1024)
        self.frameRight.pack(side=LEFT,fill=BOTH)
        # Creating a canvas
        self.canvas = Canvas(self.frameRight,width=1000)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        
        # Adding scroll bar tp Canvas
        self.scrollbar = Scrollbar(self.frameRight, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda x: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Create second frame inside the canvas
        self.second_frame =Frame(self.canvas)

        # Add second frame into a window of the canvas
        self.canvas.create_window((0,0), window=self.second_frame, anchor="nw")

        def select(e):
            listbox_value= self.listbox.get(ANCHOR)
            button_value = self.buttonClassmark.cget('text')
            searched_result = searchresult(button_value,listbox_value)
            self.result.configure(text = ' ') # clear what is inside the text and append new text
            for value in searched_result:
                self.result.configure(text=self.result.cget('text') + value + ' \n')

        self.list = getClassMarks()
        self.listbox = Listbox(self.frameLeft, height= 20, width=50)
        self.listbox.place(x=50,y=50)
        self.listbox.bind("<ButtonRelease-1>",select) 

        # get classmark from getClassMarks() function and insert it into listbox
        for classmark in self.list:
            a = self.listbox.insert(END, classmark)

        # Label to view result in self.second_frame
        self.result = Label(self.second_frame, text=' ', anchor="e", justify=LEFT, font=('default', 11, 'normal'))
        self.result.pack(side=RIGHT)
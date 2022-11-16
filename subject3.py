from tkinter import *
from tkinter import ttk
from prof import *
from gui import *

class Subject:
    def __init__(self,centerFrame):
        # Creating subject Frame
        self.subject=Frame(centerFrame,pady=100,padx=100)
        self.subject.grid(row=0,column=0,sticky='senw')
        self.img=PhotoImage(file='subject_logo4.png')
        self.imgSubject=Label(self.subject,image=self.img,padx=10,pady=10)
        self.imgSubject.pack()
        self.buttonSubject = Button(self.subject, command=self.opensubjectwindow, text='Subject Name', bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonSubject.pack()

    # Open a window for Subjet name input
    def opensubjectwindow(self):
        self.master = Toplevel()
        self.master.title('Subject Name')
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

        # Creating tree view
        self.table=ttk.Treeview(self.second_frame,columns=("Subject Name","Classmark","Location"),show='headings')
        self.table.pack(fill=BOTH)

        self.table.heading("Subject Name", text="Subject Name")
        self.table.heading("Classmark", text="Classmark")
        self.table.heading("Location", text="Location")

        self.table.column("Subject Name", anchor=W,width=10,minwidth=5)
        self.table.column("Classmark", anchor=CENTER)
        self.table.column("Location", anchor=W,width=10,minwidth=5)

        

        # Select funtion that is called after listbox selcted value is released
        def select(e):
            listbox_value= self.listbox.get(ANCHOR)
            button_value = self.buttonSubject.cget('text')
            searched_result = searchresult(button_value,listbox_value)
            # final_searched_result = [x for xs in searched_result for x in xs.split(',')]
            # Add values to tree view
            print(searched_result)
            for value in searched_result:
                # index =0
                #value.split(',')
                self.table.insert(parent='', index='end', iid=0, values=(value.split(',')[0],value.split(',')[1], value.split(',')[2]))

        # Creating listbox for Left frame
        self.list = getSubjectNames()
        self.listbox = Listbox(self.frameLeft, height= 20, width=50)
        self.listbox.place(x=50,y=50)
        self.listbox.bind("<ButtonRelease-1>",select) 
        
        # get Subject Name from getSubjectNames() function and insert it into listbox
        for subjectName in self.list:
            a = self.listbox.insert(END, subjectName)

        # Label to view result in self.second_frame
        # self.result = Label(self.second_frame, text=' ', anchor="e", justify=LEFT, font=('default', 11, 'normal'))
        # self.result.pack(side=RIGHT)

        # Adding top frame for right frame view
        self.frameview=Frame(self.second_frame,bg='blue', height=400,width=1000)
        self.frameview.pack(fill=X)


        
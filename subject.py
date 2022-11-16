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

    def getButtonValue(self):
        self.button_text = self.buttonSubject.cget('text')
        return self.button_text
        # print(self.button_text)

    # Open a window for Subjet name input
    def opensubjectwindow(self):
        SubjectWindow()
    
class SubjectWindow():
    def __init__(self):
        # super().__init__(centerFrame,button_text)
        self.master = Toplevel()
        self.master.title('Subject Name')
        self.master.geometry("1200x600+0+0")
        # Creating Left frame for new opened window
        self.frameLeft=Frame(self.master,bg='red',width=400)
        self.frameLeft.pack(side=LEFT,fill=BOTH)  
        
        # def getvalue(event):
        # print(self.clicked.get())

        # Drop down boxes
        # self.subjectclicked = StringVar()
        # self.subjectclicked.set("Select-")

        #print(self.clicked.get())

        # self.drop = ttk.Combobox(self.frameLeft,textvariable=self.subjectclicked,values=getSubjectName(), width=25,state="readonly")
        # self.drop.grid(row=1,column=1)
        # self.drop.place(x=50,y=50)
        # self.drop.bind("<<ComboboxSelected>>", checkSearhInput)

        # print(self.)
            
        # print(a)

        # Creating Right frame for new opened window

        self.frameRight=Frame(self.master,bg='green',width=800)
        self.frameRight.pack(side=LEFT,fill=BOTH)
        # Creating a canvas
        self.canvas = Canvas(self.frameRight,width=800)
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
            button_value= self.listbox.get(ANCHOR)
            self.result.configure(text=searchresult("Subject Name",button_value))
            # print(button_value)
            # print(searchresult("Subject Name",button_value))

        self.list = getSubjectNames()
        self.listbox = Listbox(self.frameLeft, height= 20, width=50)
        self.listbox.place(x=50,y=50)
        self.listbox.bind("<ButtonRelease-1>",select) 
        
        

        
        # print(Subject().getButtonValue(self))

        # self.listbox.get(ANCHOR)
        # print(self.listbox.curselection())

        for subjectName in self.list:
            a = self.listbox.insert(END, subjectName)


        self.result = Label(self.second_frame, text=' ', anchor="e", justify=LEFT, font=('default', 11, 'normal'))
        self.result.pack(side=RIGHT)

        # lambda e: self.result.configure(text=self.result.cget('text') + searchresult("Subject Name",self.listbox.get(ANCHOR))))

        # def searchResult(self, event):
        
        #     self.result.configure(text=' ')
        #     if len(self.button) < 1:
        #         self.result.configure(text='No result(s) found. Please try again.')
        #     else:
        #         self.result.configure(text='Search Result for Subject - ' + self.button + '\n\n')
        #         self.result.configure(text=self.result.cget('text') + searchresult((Subject.button_text),self.button))
          
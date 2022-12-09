from tkinter import *
from tkinter import ttk
from prof import *
from gui import *
class Location:
    def __init__(self, cf):
        # Creating location Frame
        self.location=Frame(cf,pady=100,padx=100)
        self.location.grid(row=0,column=2,sticky='senw')
        self.img3=PhotoImage(file='location_logo1.png')
        self.imgLocation=Label(self.location,image=self.img3,padx=10,pady=10)
        self.imgLocation.pack()
        self.buttonLocation = Button(self.location, command=self.openlocationwindow, text='Location', bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonLocation.pack()


    def openlocationwindow(self):
        self.master = Toplevel()
        self.master.title('Location')
        self.master.geometry("800x600+150+150")
        self.width=self.master.winfo_screenwidth()
        self.height=self.master.winfo_screenheight()
        self.master.geometry(f"{self.width}x{self.height}+0+0")
        self.master.state('zoomed')
        # Creating Left frame for new opened window
        self.frameLeft=Frame(self.master,bg='red',width=512)
        self.frameLeft.pack(side=LEFT,fill=BOTH)

        self.frameRight=Frame(self.master,bg='green')
        # pack the right frame once selection made
        self.frameRight.pack(fill=CENTER)
        
        # Add second frame into a window of the canvas
        # self.canvas.create_window((0,0), window=self.second_frame, anchor="nw")
        
        # Creating tree view
        self.table=ttk.Treeview(self.frameRight,columns=("Subject Name","Classmark","Location"),show='headings')
        

        self.table.heading("Subject Name", text="Subject Name")
        self.table.heading("Classmark", text="Classmark")
        self.table.heading("Location", text="Location")

        self.table.column("Subject Name", anchor=W,width=10,minwidth=5)
        self.table.column("Classmark", anchor=CENTER)
        self.table.column("Location", anchor=W,width=10,minwidth=5)

        # Select function that is called after listbox specified locations is released
        # def select(ef):

        # Creting scrollbar inside table
        self.scrollbar = Scrollbar(self.frameRight, orient="vertical",command=self.table.yview)

        # Select funtion that is called after listbox selcted value is released
        def select(e):
            listbox_value= self.listbox.get(ANCHOR)
            button_value = self.buttonLocation.cget('text')

            # pack tale into frame once selction made
            self.table.pack(fill=BOTH,expand=True)
            self.table.config(yscrollcommand=self.scrollbar.set)

            for row in self.table.get_children():
                self.table.delete(row)

            # pack scroll bar into right frame to attach to table
            self.scrollbar.pack(side="right", fill="y")

            # self.frameview.grid(fill=X)
            # self.canvas.create_window((0,0), window=self.second_frame, anchor="nw")

            searched_result = searchresult(button_value,listbox_value)
            # final_searched_result = [x for xs in searched_result for x in xs.split(',')]
            # Add values to tree view
            # print(searched_result)
            for value in searched_result:
                #value.split(',')
                self.table.insert(parent='', index='end', text='', values=(value.split(',')[0],value.split(',')[1].replace(' ', ', '), value.split(',')[2]))

        # Creating listbox for Left frame
        self.list = set(getLocations())
        self.listbox = Listbox(self.frameLeft, height= 20, width=50)
        self.listbox.place(x=50,y=50)
        self.listbox.bind("<ButtonRelease-1>",select) 

        # get location from getLocation() function and insert it into listbox
        for location in self.list:
            a = self.listbox.insert(END, location)

        # Adding top frame for right frame view
        # self.frameview=Frame(self.frameRight,bg='blue', height=200,width=1000)
        # self.frameview.pack(fill=X)
        # self.frameview.grid_remove() # to ensure no frame is displayed before treeview table is selected and opened
from tkinter import *
from tkinter import ttk
from prof import *
from gui import *

class Classmark:
    def __init__(self,centerFrame):         # Method sets the properties of the classmark logo selection in center frame
        # Creating location image logo on center frame
        # self.classmark=Frame(cf)
        # self.classmark.place(x=568, y= 100)
        # Creating Classmark logo
        # self.img2=PhotoImage(file='classmark_logo4.png')
        # self.imgClassmark=Label(self.classmark,image=self.img2,padx=10,pady=10)
        # self.imgClassmark.pack()
        self.img=PhotoImage(file='classmark_logo4.png')
        self.imgSubject=Label(centerFrame,image=self.img)
        self.imgSubject.place(x=728, y= 100)
        # Button for seleciton location option
        self.buttonClassmark = Button(centerFrame, command=self.openclassmarkwindow, text='Classmark', bg='#281F3E',fg='white',font=('Helvetica', 12, 'bold'),padx=10,pady=10,)
        self.buttonClassmark.place(x=748, y= 260)

    def openclassmarkwindow(self):          # Method displays the classmark window and its content from selection

        self.master = Toplevel()            # Opens new classmark window
        self.master.title('Keele Library Map - Classmark')
        self.master.iconbitmap('Keele-logo2.ico')       # Change the window icon to Keele University logo
        self.width=self.master.winfo_screenwidth()      # Gets the width of window screen
        self.height=self.master.winfo_screenheight()    # Gets the height of window screen
        self.master.geometry(f"{self.width}x{self.height}+0+0")         # Set width and heigh geometry of window
        self.master.state('zoomed')         # Ensures window is fully fit to the edges of screen
        
        # Creating left frame and placing on left side of new window
        self.frameLeft=Frame(self.master,width=512,background='#281F3E')
        self.frameLeft.pack(side=LEFT,fill=BOTH)

        # Creating right frame and placing on right side of new classmark window
        self.frameRight=Frame(self.master)
        self.frameRight.pack(fill=BOTH)
        
        # Setting backgorund image for right frame of classmark window
        self.imageBackground = PhotoImage(file='Library.png')

        self.labelBackground = Label(self.frameRight, image=self.imageBackground)            # Label created on right frame for background image
        self.labelBackground.pack(fill=BOTH)
        
        # Adding Keele university logo at top right of right frame
        self.imageLogo = PhotoImage(file='Keele logo.png')

        self.labelLogo = Label(self.frameRight, image=self.imageLogo)            # Label created on right frame for  keele logo image
        self.labelLogo.place(x=1000, y= 20)

        def button():               # Method for home button to destroy window once clicked
            self.master.destroy()

        # Create home button for left frame
        self.home_btn = Button(self.frameLeft, text="Home", font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=button,borderwidth=2)
        self.home_btn.place(x=10,y=10)

        # Styling Treeview table
        self.tablestyle = ttk.Style()
        self.tablestyle.theme_use("alt")            # selecting a specific default theme for Treeview team
        self.tablestyle.configure("Treeview", background="#281F3E", foreground="white", rowheight=40, fieldbackground='#281F3E',  font=('Helvetica', 11))
        self.tablestyle.configure("Treeview.Heading", background="#281F3E", foreground="white", font=('Helvetica', 12, 'bold'))
        
        # Creating frame for Treeview for right frame side of window
        self.frameTreeview = Frame(self.frameRight)

        # Creating Treeview
        self.table=ttk.Treeview(self.frameTreeview,columns=tuple(getAllKeys(finalTable())[0:3]),show='headings')
        self.table.config(height=20)
        
        # Creating headers and columns
        self.table.heading("Subject", text="Subject")
        self.table.heading("Classmark", text="Classmark")
        self.table.heading("Location", text="Location")

        self.table.column("Subject", anchor=W,width=5)
        self.table.column("Classmark", anchor=W,minwidth=20)
        self.table.column("Location", anchor=W,width=15)

        # Creting scrollbar for Treeview frame
        self.scrollbar = Scrollbar(self.frameTreeview, orient=VERTICAL,command=self.table.yview)

        def select(e):              # Method called after listbox selcted value is released
            
            # Gets the selected listbox classmark value
            listbox_value= self.listbox.get(ANCHOR)

            # Gets the selected button value from classmark frame
            button_value = self.buttonClassmark.cget('text')

            # Place TreeView frame for Treeview into rightframe
            self.frameTreeview.place(x=20,y=200,width=1150,height=500)

            # Pack Treeview inside TreeVIew frame
            self.table.pack(side=LEFT,fill=BOTH,expand=YES)

            # adds scroll bar into Treeview frame 
            self.table.config(yscrollcommand=self.scrollbar.set)

            # Deletes content of Treeview table
            for row in self.table.get_children():
                self.table.delete(row)

            # pack scroll bar into right frame to attach to table
            self.scrollbar.pack(side=RIGHT, fill=Y)

            # Uses searchresult() funtion to search parameter and search inputs from the user
            searched_result = searchresult(button_value,listbox_value)

            # Iterates over list of results and inserts into Treeview
            for value in searched_result:
                self.table.insert(parent='', index=END, text='', values=(value.split(',')[0],value.split(',')[1].replace(' ', ', '), value.split(',')[2]))

        # Creating frame for Listbox on left frame side of window 
        self.frameListbox = Frame(self.frameLeft)
        self.frameListbox.pack(fill=BOTH,expand=YES,pady=200,padx=20)

        # Creating listbox for Left frame
        self.list = sorted(getAllClassMarks())          # Gets all classmarks and sorts
        self.listbox = Listbox(self.frameListbox, height= 10, width=30,font=('Helvetica', 10, 'bold'),background='#595959', foreground='white', justify='center', borderwidth=5)
        self.listbox.pack(side=LEFT,fill=BOTH,expand=YES)
        self.listbox.bind("<ButtonRelease-1>",select)           # Setting an event sequence for listbox once option is selected

        # Get classmarks from getAllClassMarks() function and insert it into listbox
        for location in self.list:
            a = self.listbox.insert(END, location)

        # addding scroll bar to listbox
        self.scrollbarListbox = Scrollbar(self.frameListbox, orient=VERTICAL,command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbarListbox.set)
        self.scrollbarListbox.pack(side=RIGHT, fill=Y)
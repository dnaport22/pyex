#~PythonVersion 3.3
#Author: Navdeep Dhuti
#StudentNumber: 3433216

#importing required modules
import os
from tkinter import *
from oop.codecount import *
from oop.leastveg import *
from oop.averageheight import *
from oop.widthcounter import *
from oop.averagevotes import *
from oop.funcseven import *
from oop.numofsells import *

class FileExplorer:
    '''This Class will search for the files matching the user search and analyse
       the data in the file to answer the questions provided'''
    #Intialising 
    def __init__(self, master): #here variable master is Tk()
        self.master = master
        master.title("File Explorer")
        #initialising frames
        self.frames()
        #initialising objects/components
        self.components()
        #initialising header
        self.animation()   
    def frames(self):
        '''This is creating frames for the gui'''
        #Top of the gui
        self.anim = Canvas(self.master,height="20", width="350",bg="black")
        self.anim.grid(padx=5,pady=5)
        #Main header of the gui
        self.header = LabelFrame(self.master, text="File Explorer v0.1",font=("Magneto", 8),relief=SUNKEN,borderwidth=2,bg="#2D8BC9")
        self.header.grid(padx=5,pady=5)
        #Header top of the gui
        self.top = Frame(self.header,relief=RAISED,borderwidth=1,bg="#2D8BC9")
        self.top.grid(sticky=W+E+N+S,padx=5)
        #Below header top
        self.status = Frame(self.header,relief=SUNKEN,borderwidth=1,bg="#0D293C",width=100)
        self.status.grid(sticky=W+E+N+S,pady=5,padx=5)
        #Result window area
        self.center = LabelFrame(self.header, text="Log",bg="#2D8BC9")
        self.center.grid(sticky=W+E+N+S,padx=5)
        #Action buttons area
        self.bottom = Frame(self.header,relief=SUNKEN,borderwidth=1,bg="#ADD8E6")
        self.bottom.grid(sticky=W+E+N+S,padx=5, pady=5)

    def components(self):
        self.file = ""#this varibale will hold the file to read
        self.fileSt = StringVar()
        self.fileSt.set("None!!")#Setting default value of fileStatus
        self.defaultDir = StringVar()
        self.defaultDir.set('e')#setting default directory to read
        
        self.userInput = Entry(self.top)#This will take user input as search data
        self.userInput.insert(0,'Search for file...')#Default value of input field
        self.userInput.grid(row=1,padx=5)
        self.findBtn = Button(self.top, text="Search", command=self.searchFile,bg="#80b929",font=("Helvetica",10))#Execute the searchFile function
        self.findBtn.grid(row=1,column=2,pady=5,padx=5)
        self.clearLog = Button(self.top,text="Clear Log",command=self.clearLog,bg="#0D293C",fg="#fff")#execute clearLog function and clear result window
        self.clearLog.grid(row=1,column=3,padx=5)
        self.closeFile = Button(self.top,text="Close File",command=self.closeFile,bg="#0D293C",fg="#fff")#execute closeFile function and close any open file
        self.closeFile.grid(row=1,column=4,padx=5)

        self.scrollbar = Scrollbar(self.center, orient="vertical")#scroll bar for result window
        self.scrollbar.grid(column=2,sticky=N+S)#positioning scroll bar
        self.resultWin = Listbox(self.center, width="50",yscrollcommand=self.scrollbar.set,cursor="hand2")#creating result window and adding scroll bar
        self.resultWin.grid(row=0,column=0,rowspan=1,columnspan=1,padx=5)
        self.resultWin.config(yscrollcommand = self.scrollbar.set)
        self.resultWin.bind('<<ListboxSelect>>',self.valSelect)#making the strings in list box clickable 
        self.scrollbar.config(command = self.resultWin.yview)
        
        self.readFileBtn = Button(self.bottom,text=" Read File ",command=self.readFile,bg="#0D293C",fg="#fff")#execute readFile function
        self.readFileBtn.grid(row=1,column=1,padx=5)
        arrow = Label(self.bottom,text=">>",bg="#ADD8E6",fg="#0D293C").grid(padx=10,row=1,column=2)#creating arrows '>>'
        self.analyseBtn = Button(self.bottom,text="Analyse Data",command=self.Results,bg="#0D293C",fg="#fff")#execute Results function
        self.analyseBtn.grid(row=1,column=3,padx=5)
        arrow = Label(self.bottom,text=">>",bg="#ADD8E6",fg="#0D293C").grid(padx=10,row=1,column=4)#creating arrows '>>'
        self.ansCardBtn = Button(self.bottom, text="Generate Card",command=self.cardFunc,bg="#0D293C",fg="#fff")#execute cardFunc
        self.ansCardBtn.grid(row=1,column=5,pady=5,padx=5)
    
        self.fileStatusLb = Label(self.status,text="Reading File:",borderwidth=1,bg="#0D293C",fg="#fff")
        self.fileStatusLb.grid(row=1,padx=5,pady=5)
        self.StColor = StringVar()
        self.StColor.set("#E5E544") #Default color of fileStatusSt label
        self.fileStatusSt = Label(self.status,textvariable=self.fileSt,relief=SUNKEN,borderwidth=1,bg=self.StColor.get(),width=15)
        self.fileStatusSt.grid(row=1,column=1,pady=5)
        self.readDir = Label(self.status,text='Reading Directory:',borderwidth=1,bg="#0D293C",fg="#fff")
        self.readDir.grid(row=1,column=2,pady=5,padx=10)
        self.readDirInput = Entry(self.status,textvariable=self.defaultDir,relief=SUNKEN,borderwidth=1,width=3)#input directory path
        self.readDirInput.grid(row=1,column=3,pady=5)
                
    def searchFile(self):
        '''This class will search for the file in the provided directory
        except FileNotFoundError and display message to the user'''
        dirInput = self.readDirInput.get()#Take the input from readDirInput variable
        try:
            for file in os.listdir(dirInput+':'):
                file.startswith(self.userInput.get())#serach for the file names starting with the input value
                self.resultWin.insert(END,file)#displaying the results in resultWin
        except FileNotFoundError:#if file does not exist of the path is invalid
                #Displays these messages in state of error
                self.resultWin.insert(END,'Error: Cannot locate the directory')
                self.resultWin.insert(END,'Please input a valid directory')
                  
    def valSelect(self,evt):
        '''For results in resultWin, users click on the string displayed and
           program store it in a variable then use it as file name'''
        value=str((self.resultWin.get(ACTIVE)))#stringify the selected value in resultWin
        doc_in = open(value)#open file 
        self.file = value
        self.StColor.set("#5DAE5D")#define status colour to green
        self.fileStatusSt.configure(bg=self.StColor.get())#change status colour
        self.fileSt.set(value)#insert file name into reading file label
        
        print(self.file)#prints the selected file name in IDLE for debugging
        
    def Results(self):#giving an output with results
        '''Execute the functions from the files imported'''
        self.ansList = []#Storing answers from return values of the functions
        try:
            doc_in = (self.file)
            file = open(doc_in)
            file.close()
            doc = (doc_in)
            veg = leastVeg(doc_in)
            code = codeCounter(doc_in)
            ave_height = averageHeight(doc_in)
            width = widthCounter(doc_in)
            ave_votes = averageVotes(doc_in)
            seven = funcSeven(doc_in)
            sells = numofSells(doc_in)
            self.resultWin.delete(0,END)
            self.resultWin.insert(END,"Click on Generate Card to View all Answers")
            #appending all the return values to self.ansList list 
            self.ansList.append(code.match())
            self.ansList.append(veg.leastVegResult())
            self.ansList.append(ave_height.average())
            self.ansList.append(width.Width_counter())
            self.ansList.append(ave_votes.Average_votes())
            self.ansList.append(seven.func_seven())
            self.ansList.append(sells.NumofSells())
        except FileNotFoundError:
            self.resultWin.insert(END, doc_in+' '+'File Error, Try Again!!' )
        return file
    
    def openFile(self):
        '''open the file so that it can be used throughout the application'''
        try:
            doc_in = (self.file)
            doc = open(self.file)
            self.resultWin.insert(END, doc_in+' '+'is Open Now' )
        except FileNotFoundError:
            self.resultWin.insert(END, doc_in+' '+'Not Found, Try Again!!' )
        return doc
    
    def readFile(self):
        '''This displays the file data in list box view in the application'''
        self.resultWin.delete(0,END)
        doc_in = self.openFile()
        for data in doc_in:
            data = data.strip().split(',')
            self.resultWin.insert(END,data)
                
    def closeFile(self):
        '''closing any open file'''
        self.resultWin.delete(0,END)
        doc_open = open(self.file,'r')
        doc_open.close()
        self.resultWin.insert(END, self.file+' '+'is Closed Now' )
        self.fileSt.set("None!!")
        self.StColor.set("#E5E544")
        self.fileStatusSt.configure(bg=self.StColor.get())
        self.file = ''
        
    def clearLog(self):
        '''Clearing result screen'''
        self.resultWin.delete(0,END)

    def cardFunc(self):
        '''opeining anotheer window to view all the answers in one place'''
        card = Toplevel()
        card.resizable(0,0)
        card.title("File Explorer || Card View")
        card.configure(bg="#ADD8E6")
        for questions in self.ansList:
            '''Repeating the Frame element according the number of return values and
             splitting questions and anwers in the self.ansList list'''
            myQues = StringVar()
            myQues.set(questions[0])#first part of the return values stored in self.ansList list are questions
            cardFrame = Frame(card,relief=RAISED,width="300",height="50",borderwidth=5 ,bg="#0D293C")
            cardFrame.grid(sticky=W+E+N+S,padx=10,pady=5)
            qus = Label(cardFrame,textvariable=myQues,bg="#0D293C",fg="#fff")
            qus.grid(row=1,sticky=W,pady=5)
            myAns = StringVar()
            myAns.set(questions[1])#Second part of the return values stored in self.ansList list are questions
            ans = Label(cardFrame,textvariable=myAns,bg="#5DAE5D",borderwidth=2,relief=SUNKEN,width=18)
            ans.grid(row=1,column=2,sticky=E)
    def animation(self):
        '''Displays the top heading within the applications'''
        string = self.anim.create_text(180,10,text="Created By: Navdeep Dhuti || For: Software Development 2")
        self.anim.itemconfig(string,fill="green")
                

   
root = Tk()
root.configure(bg="#2D8BC9")
file_ex = FileExplorer(root)
root.resizable(0,0)
root.mainloop()

#creating notepad using GUI 
from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename 
import os 
def newFile():
    global file
    root.title("Untitled-Notepad!")
    file = None 
    textArea.delete(1.0,END)

def openFile():
    global file 
    file = askopenfilename(defaultextension = ".txt",filetypes =[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None 
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0,END)
        f = open(file,"r")
        textArea.insert(1.0,f.read()) 
        f.close()
        

def saveFile():
    global file 
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt",defaultextension = ".txt",filetypes =[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None 
        else:
            #save as fileName 
            f = open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close() 
            root.title(os.path.basename(file) + " - Notepad")
    else:
        #save the existing file
        f = open(file,"w")
        f.write(textArea.get(1.0,END))
        f.close() 
        

def exitApp():
    root.destroy()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>")) 

def about():
    showinfo("Notepad!","Created and designed by GREPPERMEDIA")
    
def Arial():
    global textArea 
    textArea.config(font = "Arial")

def Helvetica():
    global textArea
    textArea.config(font = "Helvetica")

def Cambria():
    global textArea
    textArea.config(font = "Cambria")

def Courier():
    global textArea
    textArea.config(font = "Courier")

def dateandTime():
    import time 
    global textArea 
    local_time = time.asctime(time.localtime(time.time()))
    textArea.insert('end',f"{local_time}")

def bold():
    global textArea 
    textArea.config(font = "Arial 15 bold") 
    
    
if __name__ == "__main__":
    root = Tk()
    root.title("Notepad!")
    root.wm_iconbitmap("color-icon2.ico")
    root.geometry("644x568")
    #ADDING TEXT AREA 
    textArea = Text(root,font = "lucida 13")
    file = None 
    textArea.pack(fill = BOTH,expand = TRUE)
    #CREATING MENUBAR 
    menuBar = Menu(root)
    #Creating File menu
    fileMenu = Menu(menuBar,tearoff = 0)
    #ADD option in fileMenu
    #for opening a new file
    fileMenu.add_command(label = "New",command = newFile)
    #for opening a existing file 
    fileMenu.add_command(label = "Open",command = openFile)
    #for saving the current file 
    fileMenu.add_command(label = "Save",command = saveFile)
    #add separator 
    fileMenu.add_separator()
    #exit option 
    fileMenu.add_command(label = "Exit",command = exitApp)
    #final fileMenu 
    menuBar.add_cascade(label = "File",menu = fileMenu)
    #Creating Edit menubar 
    editMenu = Menu(menuBar,tearoff = 0)
    #adding features like cut,copy and paste,date and Time 
    editMenu.add_command(label = "Cut",command = cut)
    editMenu.add_command(label = "Copy",command = copy)
    editMenu.add_separator()
    editMenu.add_command(label = "Paste",command = paste)
    editMenu.add_command(label = "Bold",command = bold)
    editMenu.add_command(label = "date/time",command = dateandTime)
    #Creating a fontMenu 
    fontMenu = Menu(editMenu,tearoff = 0)
    fontMenu.add_command(label = "Arial",command = Arial)
    fontMenu.add_command(label = "Helvetica",command = Helvetica)
    fontMenu.add_separator()
    fontMenu.add_command(label = "Cambria",command = Cambria)
    fontMenu.add_command(label = "Courier",command = Courier)
    editMenu.add_cascade(label = "Font",menu = fontMenu)
    menuBar.add_cascade(label = "Edit",menu = editMenu)
    #Creating Help menubar 
    helpMenu = Menu(menuBar,tearoff = 0)
    #Adding a option like About us 
    helpMenu.add_command(label = "About us",command = about)
    menuBar.add_cascade(label = "Help",menu = helpMenu)
    #Addinng a ScrollBar 
    scrollBar = Scrollbar(textArea)
    scrollBar.pack(side = RIGHT,fill = Y)
    scrollBar.config(command = textArea.yview)
    textArea.config(yscrollcommand = scrollBar.set)
    root.config(menu = menuBar)
    root.configure(background = "white")
    root.mainloop()

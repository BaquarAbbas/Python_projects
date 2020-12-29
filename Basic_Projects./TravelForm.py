#TRAVELFORM USING GUI
from tkinter import * 
root = Tk() 
root.geometry("444x344")
#HEADING
Label(root,text = "Welcome to barry travels",font = "comicsansms 13 bold",pady = 16).grid(row = 0,column = 3)
#LABELS
Name = Label(root,text="Name",pady = 2)
Phone = Label(root,text="Phone",pady = 2)
Gender = Label(root,text="Gender",pady = 2)
Emergency = Label(root,text="EmergencyContact",pady = 2)
PaymentMode = Label(root,text="PaymentMode",pady = 2)
#PACK TEXT USIG GRID
Name.grid(row = 1,column = 2)
Phone.grid(row = 2,column = 2)
Gender.grid(row = 3,column = 2)
Emergency.grid(row = 4,column = 2)
PaymentMode.grid(row = 5,column = 2)
#TKINTER VARIABLES FOR STORING VALUES
Name_val = StringVar() 
Phone_val = StringVar() 
Gender_val = StringVar() 
Emergency_val = StringVar() 
Payment_val = StringVar() 
foodservice_val = IntVar()
#ENTRIES FOR LABELS
Name_entry = Entry(root,textvariable=Name_val)
Phone_entry = Entry(root,textvariable=Phone_val)
Gender_entry = Entry(root,textvariable=Gender_val)
Emergency_entry = Entry(root,textvariable=Emergency_val)
Payment_entry = Entry(root,textvariable=Payment_val)
#PACKING ENTRIES
Name_entry.grid(row = 1,column =3 )
Phone_entry.grid(row = 2,column =3 )
Gender_entry.grid(row = 3,column =3 )
Emergency_entry.grid(row = 4,column =3 )
Payment_entry.grid(row = 5,column =3 )
#CHECKBUTTON PACKING AND CREATION 
foodservice = Checkbutton(text = "Do you want to prebook your meals?",variable = foodservice_val)
foodservice.grid(row = 6 ,column = 3)
#STOREVALS FUNCTION 
def storeVals():#Information gets updated into file when you will click the button
    print(f"{Name_val.get(),Phone_val.get(),Gender_val.get(),Emergency_val.get(),Payment_val.get(),foodservice_val.get()}")
    
    with open("Travels_record.txt","a") as f:
        f.write(f"{Name_val.get(),Phone_val.get(),Gender_val.get(),Emergency_val.get(),Payment_val.get(),foodservice_val.get()}\n")
    
Button(text = "Submit",command = storeVals).grid(row = 7,column = 3)
root.mainloop()

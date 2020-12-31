#CORONA TRACKER USING GUI
#Fetches data from the given URL and displays the results 
from tkinter import *
import requests
from bs4 import BeautifulSoup 
url = "https://www.worldometers.info/coronavirus/"
page = requests.get(url)
Soup = BeautifulSoup(page.content,"html.parser")
info = Soup.find_all(class_ = "maincounter-number")
a = [items.get_text() for items in info]


root = Tk()
root.title("Corona virus report")
root.geometry("500x700")

font = ("helvetica",12,"bold")

country = ""
def find_info():
    country = C.get()
    url1 = "https://www.worldometers.info/coronavirus/country/" + country
    page1 = requests.get(url1)
    Soup1 = BeautifulSoup(page1.content,"html.parser")
    info1 = Soup1.find_all(class_ = "maincounter-number")
    b= [items.get_text() for items in info1]
    
    label1 = Label(root,text = "Total cases of corona virus in " + country,font = font)
    label1.pack()
    label2 = Label(root,text = b[0],font = font)
    label2.pack()
    label3 = Label(root,text = "Total deaths of corona virus in " + country,font = font)
    label3.pack()
    label4 = Label(root,text = b[1],font = font)
    label4.pack()
    label5 = Label(root,text = "Total Recoverd cases of corona virus in "+ country,font = font)
    label5.pack()
    label6 = Label(root,text = b[2],font = font)
    label6.pack()


label1 = Label(root,text = "Total cases of corona virus",font = font)
label1.pack()
label2 = Label(root,text = a[0],font = font)
label2.pack()
label3 = Label(root,text = "Total deaths of corona virus",font = font)
label3.pack()
label4 = Label(root,text = a[1],font = font)
label4.pack()
label5 = Label(root,text = "Total Recoverd cases of corona virus",font = font)
label5.pack()
label6 = Label(root,text = a[2],font = font)
label6.pack()
label6 = Label(root,text = "Please type your country name ",font = font)
label6.pack()

C = Entry(root,font = font)
C.pack(pady = 10)

button1= Button(root,text = "Find info",font = font,bg = "blue",command = find_info)
button1.pack()

root.mainloop()

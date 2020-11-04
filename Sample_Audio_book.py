#You need to install these two packages
#1.pyPDF2
#2.pyttsx3
#you can use any pdf file

import PyPDF2
import pyttsx3
book = open('FiveTypesofEssays.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
speaker.say('Hi,Munna I am here to help you')
for num in range(1,pages):
    page = pdfReader.getPage(num)
    text  = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
book.close()

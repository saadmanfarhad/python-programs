import PyPDF2
import os

os.chdir('/home/saadmanfarhad/Projects/Python')
pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

for i in range(reader.numPages):
    print(reader.getPage(i).extractText())

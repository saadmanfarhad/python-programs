import PyPDF2
import os

os.chdir('/home/saadmanfarhad/Projects/Python')
pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)
writer = PyPDF2.PdfFileWriter()

for i in range(reader1.numPages):
    page = reader1.getPage(i)
    writer.addPage(page)

for i in range(reader2.numPages):
    page = reader2.getPage(i)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()

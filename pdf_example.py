import PyPDF2, os

os.chdir('c:\\users\al\\documents')

pdfFile = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)
reader.numPages

page = reader.getPage(0)
# pages start at 0

page.extractText()

for pageNum in range(read.numPages):
    print(reader.getPage(pageNum).extractText())



# importing all the required modules
from PyPDF3 import PdfFileWriter, PdfFileReader

# creating a pdf file object
pdfFileObj = open('Tammo.pdf')

# creating a pdf reader object
pdfReader = PdfFileReader(pdfFileObj)

# creating a page object
pageObj = pdfReader.getPage(22)
page_content = pageObj.extractText()
# extracting text from page
print( page_content.encode('utf-8'))

# closing the pdf file object
pdfFileObj.close()
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

document = open('Tammo.pdf', 'rb')
#Create resource manager
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
i=0
for page in PDFPage.get_pages(document):
    i += 1

    interpreter.process_page(page)
    # receive the LTPage object for the page.
    layout = device.get_result()
    print("-----------------------  Page: " + str(i) + " -------------------")
    for element in layout:
        if isinstance(element, LTTextBoxHorizontal):
            print(element)

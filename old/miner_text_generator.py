import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def extract_text_by_page(pdf_path):
    i = 0
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
            i += 1
            text = "\n-----------------------  Page: " + str(i) + " -------------------\n"
            text = text + fake_file_handle.getvalue()
            yield text

            # close open handles
            converter.close()
            fake_file_handle.close()


def extract_text(pdf_path):
    f = open("Tammo.txt", "a", encoding="utf-8-sig")
    for page in extract_text_by_page(pdf_path):
        print(page)
        print()
        f.write(page)
        f.write("\n\n")
    f.close()

if __name__ == '__main__':
    print(extract_text('Tammo.pdf'))
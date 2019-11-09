from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from Manifest  import Manifest
from utils import ItemBBOX, my_functions
import math, datetime, traceback

Manifests = []
LastBOL = '0'

def parse_pdf(path,pages = 134):
    global LastBOL

    try:
        pdf_file = open(path, 'rb')

        #Create PDF Parser
        rsrcmanager  = PDFResourceManager()
        PDFPageAgg = PDFPageAggregator(rsrcmanager, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmanager, PDFPageAgg)
        for n, page in enumerate(PDFPage.get_pages(pdf_file, maxpages=pages, password="",caching=True)):
            n += 1
            print('###### page ' + str(n))
            myTEUs = 0
            myWeight = 0
            interpreter.process_page(page)
            # receive the LTPage object for the page.
            LTPage_layout = PDFPageAgg.get_result()
            myBOL = get_BOL_from_elements(LTPage_layout)
            if not myBOL:
                print("Empty Page " + "\n")
                continue

            if LastBOL == myBOL:
                myTEUs, myWeight = get_TEUs_from_elements(LTPage_layout)
                if myTEUs == 0:
                    print("Continue same BOL: " + myBOL + "\n")
                    continue
                else:
                   myManifest.TEUs = myTEUs
                   myManifest.WeightORG_Tonne = myWeight

            else:
                myManifest = Manifest()
                myManifest.BOL = myBOL
                get_text_from_elements(LTPage_layout, myManifest)


            if myManifest.TEUs > 0:
                myManifest.SetCalculatedValues()
                myManifest.myPrint()
                Manifests.append(myManifest.get_list())
                print("-------------------------------------")
            else:
                print("Continue same BOL: " + myBOL + "\n")
            myTEUs = 0
            LastBOL = myBOL

        pdf_file.close()
        PDFPageAgg.close()
    except Exception: traceback.print_exc()

def get_BOL_from_elements(layout):
    myBOL = ''
    for element in layout:
        try:
            element_bbox0 = math.floor(element.bbox[0])
            element_bbox1 = math.floor(element.bbox[1])
            #BOL
            if element_bbox0 == ItemBBOX.BOL[0] and element_bbox1 == ItemBBOX.BOL[1]:
                myBOL = element.get_text().splitlines()[ItemBBOX.BOL[2]]

        except Exception: traceback.print_exc()
    return myBOL

def get_TEUs_from_elements(layout):
    myTEUs = 0
    myWeight = 0
    for element in layout:
        try:
            # TEUs
            element_bbox0 = math.floor(element.bbox[0])

            if element_bbox0 == ItemBBOX.TEUs[0]:
                myTEUs = int(element.get_text().splitlines()[ItemBBOX.TEUs[2]].strip())
                # WeightORG_Tonne
            elif element_bbox0 == ItemBBOX.WeightORG_Tonne[0]:
                myWeight = float(element.get_text().splitlines()[ItemBBOX.WeightORG_Tonne[2]].strip())

        except Exception: traceback.print_exc()
    return myTEUs, myWeight

def get_text_from_elements(layout, myManifest):
    for element in layout:
        try:
            if not isinstance(element, LTTextBoxHorizontal):
                continue

            element_bbox0 = math.floor(element.bbox[0])
            element_bbox1 = math.floor(element.bbox[1])
            element_bbox2 = math.floor(element.bbox[2])
            element_bbox3 = math.floor(element.bbox[3])
            text_lines =element.get_text().splitlines()

            #Shipping_Line
            if element_bbox0 == ItemBBOX.Shipping_Line[0] and element_bbox1 == ItemBBOX.Shipping_Line[1]:
                myManifest.Shipping_Line = text_lines[ItemBBOX.Shipping_Line[2]]

            #Shipper
            elif element_bbox0 == ItemBBOX.Shipper[0] and element_bbox3 == ItemBBOX.Shipper[1]:
                myManifest.Shipper = text_lines[ItemBBOX.Shipper[2]].replace('SH:','').strip()
                len_lines= len(text_lines)
                # Shipper_Location_City
                if len_lines > 1:
                    places = my_functions.extract_locations(text_lines)

                    # Shipper_Location_City
                    myManifest.Shipper_Location_City = places[1]
                    # Shipper_Location_Country
                    myManifest.Shipper_Location_Country = places[0]

                    #myManifest.Shipper_Location_City = text_lines[len_lines - 2]
                    # Shipper_Location_Country
                    #myManifest.Shipper_Location_Country = text_lines[len_lines - 1]

            # Shipper_Location_City
            elif element_bbox0 == ItemBBOX.Shipper_Location_City[0] and element_bbox3 == ItemBBOX.Shipper_Location_City[1]:
                places = my_functions.extract_locations(text_lines)
                # Shipper_Location_City
                myManifest.Shipper_Location_City = places[1]
                # Shipper_Location_Country
                myManifest.Shipper_Location_Country = places[0]

                # Shipper_Location_City
                #myManifest.Shipper_Location_City = text_lines[len(text_lines)-2]
                # Shipper_Location_Country
                #myManifest.Shipper_Location_Country = text_lines[len(text_lines)-1]

            # Cont_Size
            elif element_bbox0 == ItemBBOX.Cont_Size[0] and element_bbox2 == ItemBBOX.Cont_Size[1]:
                myManifest.Cont_Size = int(text_lines[ItemBBOX.Cont_Size[2]].replace('SZTP:','').strip()[:2])
            elif element_bbox0 == ItemBBOX.Cont_Size_value[0] and element_bbox2 == ItemBBOX.Cont_Size_value[1]:
                myManifest.Cont_Size = int(text_lines[ItemBBOX.Cont_Size[2]].strip()[:2])

            # WeightORG_Tonne
            elif element_bbox0 == ItemBBOX.WeightORG_Tonne[0]:
                myManifest.WeightORG_Tonne = float(text_lines[ItemBBOX.WeightORG_Tonne[2]].strip())

            # TEUs
            elif element_bbox0 == ItemBBOX.TEUs[0]:
                myManifest.TEUs = int(text_lines[ItemBBOX.TEUs[2]].strip())

            # Commodity
            elif element_bbox0 == ItemBBOX.Commodity[0] and element_bbox1 == ItemBBOX.Commodity[1]:
                myManifest.Commodity = text_lines[ItemBBOX.Commodity[2]] +  text_lines[1]

            # Consignee
            elif element_bbox0 == ItemBBOX.Consignee[0] and element_bbox1 == ItemBBOX.Consignee[1]:
                myManifest.Consignee = text_lines[ItemBBOX.Consignee[2]].replace('CN:','').strip()

            # Actual_Port_of_Loading
            elif element_bbox0 == ItemBBOX.Actual_Port_of_Loading[0] and element_bbox1 == ItemBBOX.Actual_Port_of_Loading[1]:
                myManifest.Actual_Port_of_Loading = text_lines[ItemBBOX.Actual_Port_of_Loading[2]].replace('CN:','').strip()

            # Place_delivery_City & Actual_Port_Discharge_City
            elif element_bbox0 == ItemBBOX.Place_delivery_City[0] and element_bbox1 == ItemBBOX.Place_delivery_City[1]:
                myManifest.Place_delivery_City = text_lines[ItemBBOX.Place_delivery_City[2]]
                myManifest.Actual_Port_Discharge_City = text_lines[ItemBBOX.Actual_Port_Discharge_City[2]]

            # Date_of_Arrival
            elif element_bbox0 == ItemBBOX.Date_of_Arrival[0] and  element_bbox1 == ItemBBOX.Date_of_Arrival[1]:
                myManifest.Date_of_Arrival = datetime.datetime.strptime(text_lines[ItemBBOX.Date_of_Arrival[2]],'%d-%b-%y')

        except Exception: traceback.print_exc()

if __name__ == '__main__':
    parse_pdf('Tammo.pdf',150)
    my_functions.export_csv(Manifests)
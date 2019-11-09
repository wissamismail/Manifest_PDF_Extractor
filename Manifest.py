import datetime
from utils import ItemBBOX, my_functions
import traceback
class Manifest:

  def __init__(self):
    self.BOL = ''

    self.Shipping_Line = ''
    self.Shipper = ''
    self.Shipper_Location_City = ''
    self.Shipper_Location_Country = ''

    self.Commodity_Code = '140-639'

    self.Cont_Size = 0
    self.TEUs = 0
    self.Splits = ''
    self.WeightORG_Tonne = 0

    self.Package_Class = 'Containerized'

    self.Commodity = ''
    self.Consignee = ''

    self.Actual_Port_of_Loading = ''

    self.Place_delivery_City = ''
    self.Place_delivery_Country = ''

    self.Actual_Port_Discharge_City = ''
    self.Actual_Port_Discharge_Country = ''

    self.Date_of_Arrival = datetime.datetime.now()
    self.Month = self.Date_of_Arrival.month
    self.Year = self.Date_of_Arrival.year
    self.Manifest_Type = 'Export'
    self.Page_number = 1
    self.Pages_count = 0

  def SetCalculatedValues(self):
      try:
        self.Date_of_Arrival = datetime.datetime.date(self.Date_of_Arrival)
        self.Month = self.Date_of_Arrival.month
        self.Year = self.Date_of_Arrival.year
        self.Place_delivery_Country = my_functions.extract_country(self.Place_delivery_City)
        self.Actual_Port_Discharge_Country = my_functions.extract_country(self.Actual_Port_Discharge_City)
        if self.Cont_Size == 40:
           self.TEUs = 2 * self.TEUs
      except Exception:
        traceback.print_exc()

  def get_list(self):
    theList = []

    theList.append(self.Shipping_Line)
    theList.append(self.Shipper)
    theList.append(self.Shipper_Location_City)
    theList.append(self.Shipper_Location_Country)
    theList.append(self.Commodity_Code)
    theList.append(self.Cont_Size)
    theList.append(self.TEUs)
    theList.append(self.Package_Class)
    theList.append(self.WeightORG_Tonne)
    theList.append(self.Commodity)
    theList.append(self.BOL)
    theList.append(self.Consignee)
    theList.append(self.Actual_Port_of_Loading)
    theList.append(self.Place_delivery_City)
    theList.append(self.Place_delivery_Country)
    theList.append(self.Actual_Port_Discharge_City)
    theList.append(self.Actual_Port_Discharge_Country)
    theList.append(self.Date_of_Arrival)
    theList.append(self.Month)
    theList.append(self.Year)
    theList.append(self.Manifest_Type)
    return theList

  def myPrint(self):
    print("{}\t\t\t\t\t\t=\t{}".format('BOL ' , self.BOL))
    print("{}\t\t\t\t=\t{}".format('Shipping_Line ' , self.Shipping_Line))
    print("{}\t\t\t\t\t=\t{}".format('Shipper ' , self.Shipper))
    print("{}\t\t=\t{}".format('Shipper_Location_City ' , self.Shipper_Location_City))
    print("{}\t=\t{}".format('Shipper_Location_Country ' , self.Shipper_Location_Country))
    print("{}\t\t\t\t\t=\t{}".format('Cont_Size ' , self.Cont_Size))
    print("{}\t\t\t\t\t\t=\t{}".format('TEUs ' , self.TEUs))
    print("{}\t\t\t=\t{}".format('WeightORG_Tonne ' , self.WeightORG_Tonne))
    print("{}\t\t\t\t\t=\t{}".format('Commodity ' , self.Commodity))
    print("{}\t\t\t\t\t=\t{}".format('Consignee ' , self.Consignee))
    print("{}\t\t=\t{}".format('Actual_Port_of_Loading ' , self.Actual_Port_of_Loading))
    print("{}\t\t=\t{}".format('Place_delivery_City ' , self.Place_delivery_City))
    print("{}\t\t=\t{}".format('Place_delivery_Country ', self.Place_delivery_Country))
    print("{}\t=\t{}".format('Actual_Port_Discharge_City ' , self.Actual_Port_Discharge_City))
    print("{}=\t{}".format('Actual_Port_Discharge_Country ', self.Actual_Port_Discharge_Country))
    print("{}\t\t\t=\t{}".format('Date_of_Arrival ' , self.Date_of_Arrival))
    print("{}\t\t\t\t\t\t=\t{}".format('Month ' , self.Month))
    print("{}\t\t\t\t\t\t=\t{}\n".format('Year ' , self.Year))


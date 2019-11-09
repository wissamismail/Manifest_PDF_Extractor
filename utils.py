import csv, sys, traceback
from geotext import GeoText
from geopy.geocoders import Nominatim

class ItemBBOX:
    BOL                         = [77, 466, 2]
    Shipping_Line               = [78, 530, 0]
    Shipper                     = [67, 459, 0]
    Shipper_Location_City       = [86, 448, 1]
    Shipper_Location_Country    = [67, 420, 2]

    Cont_Size                   = [363, 405, 1]
    Cont_Size_value             = [388, 405, 1]
    WeightORG_Tonne1             = [491, 414, 0]
    WeightORG_Tonne             = [490, 527 ,0]
    Commodity                   = [332, 414, 0]
    Consignee                   = [67 , 372, 0]
    Actual_Port_of_Loading      = [353, 520, 0]

    Place_delivery_City         = [650, 507, 2]
    Actual_Port_Discharge_City  = [650, 507, 0]
    Date_of_Arrival             = [644, 559, 1]
    TEUs_Total                  = [285, 323, 0]
    TEUs                        = [324, 328, 1]

class my_functions:
    header_list = ['Shipping Line', 'Shipper',
                   'Shipper Location - City,Province', 'Shipper Location - Country',
                   'Commodity Code', 'Cont. Size', 'TEU''s', 'Package Class',
                   'Weight (ORG) in Tonne', 'Commodity', 'BOL #', 'Consignee',
                   'Actual Port of Loading', 'Place of delivery-City,Province',
                   'Place of delivery- Country', 'Actual Port of Discharge-City,Province',
                   'Actual Port of Discharge- Country', 'Date of Arrival', 'Month', 'Year', 'Manifest Type'
                   ]

    def export_csv(Manifests):
        try:
            Manifests.insert(0, my_functions.header_list)
            with open('myManifest.csv', 'w', newline='', encoding="utf-8") as csvFile:
                writer = csv.writer(csvFile)
                writer.writerows(Manifests)
            csvFile.close()
        except Exception: traceback.print_exc()

    def extract_locations(mytext):
        try:
            myPlaces = ['','']
            for text in mytext:
                places = GeoText(text.title())
                if places.countries:
                    myPlaces[0]= places.countries[0]
                if places.cities:
                    myPlaces[1]= places.cities[0]
            return myPlaces
        except Exception: traceback.print_exc()


    def extract_country(mytext):
        try:
            if not hasattr(my_functions.extract_country, "geolocator"):
                my_functions.extract_country.geolocator=Nominatim(timeout=5)  # it doesn't exist yet, so initialize it
            loc = my_functions.extract_country.geolocator.geocode(mytext.replace('*',''))
            #
            address = loc.address.split(",")
            return address[len(address)-1].strip()

        except Exception:
            print("----------------------------------" + mytext)
            traceback.print_exc()
            exit()


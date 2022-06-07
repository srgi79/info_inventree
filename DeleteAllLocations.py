from inventree.api import InvenTreeAPI
from inventree.stock import StockLocation

SERVER_ADDRESS = 'http://192.168.31.100:8000'
MY_USERNAME = 'USER'
MY_PASSWORD = 'PASSWORD'

api = InvenTreeAPI(SERVER_ADDRESS, username=MY_USERNAME, password=MY_PASSWORD)

locationsList = StockLocation.list(api)
#print("locationsList", locationsList)


nLocations = len(locationsList)
if nLocations > 0:
    print("DELETING ALL STOCK LOCATIONS")
    for idx in range(nLocations):
      print("Deleting location number", idx, ": ", locationsList[idx].pk)
      locationsList[idx].delete()
else:
    print("NO STOCK LOCATIONS")
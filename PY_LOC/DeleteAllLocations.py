
#docker compose run --rm inventree-server invoke delete-data
#docker compose run --rm inventree-server invoke setup-test -i

from inventree.api import InvenTreeAPI
from inventree.stock import StockLocation
import yaml

with open('_Locations.yaml', 'r') as file:
    cfg = yaml.safe_load(file)

api = InvenTreeAPI(cfg['SERVER']['URL'], username=cfg['SERVER']['USER'], password=cfg['SERVER']['PWD'])

locationsList = StockLocation.list(api)


nLocations = len(locationsList)
if nLocations > 0:
    print("DELETING ALL STOCK LOCATIONS")
    for idx in range(nLocations):
      print("Deleting location number", idx, ": ", locationsList[idx].pk)
      locationsList[idx].delete()
else:
    print("NO STOCK LOCATIONS")

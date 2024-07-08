from inventree.api import InvenTreeAPI
from inventree.stock import StockLocation
import yaml

ASCII_START = 65

with open('_Locations.yaml', 'r') as file:
    cfg = yaml.safe_load(file)

api = InvenTreeAPI(cfg['SERVER']['URL'], username=cfg['SERVER']['USER'], password=cfg['SERVER']['PWD'])

"""
for k, v in cfg['LOC'].items():
    print(k, v)
    print(type(k), type(v))
"""
# CREATE STRUCTURAL LOCATION
loc = cfg['LOC']['STRUCTURAL']
if ("NAME" in loc) and ("DESC" in loc):
    print("Creating Structural Location ", loc)
    structural = StockLocation.create(api, {'name':loc["NAME"], 'description':loc["DESC"], 'parent':'', 'structural': True})
else:
    print("Cannot Create Structural Location ", loc)

# CREATE SHELV LOCATIONS
loc = cfg['LOC']['SHELVS']
locs = []
for k, v in loc.items():
    # MANUAL ENTRIES
    if type(v) == list:
        for e in v:
            locs.append(e)
    # GENERATING ENTRIES
    elif type(v) == dict:
        for i in range(v['V']):
            for j in range(1, v['H']+1):
                s = k + chr(i+ASCII_START) + str(j)
                locs.append(s)
                #print(f"Creating shelv {s}")

locs.sort()
#print(locs)

for loc in locs:
    print("Creating Shelv Location ", loc)
    StockLocation.create(api, {'name':loc, 'description':'', 'parent':structural.pk})




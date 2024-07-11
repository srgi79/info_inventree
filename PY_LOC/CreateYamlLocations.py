from inventree.api import InvenTreeAPI
from inventree.stock import StockLocation
import yaml, requests

ASCII_START = 65 #A

with open('_Locations.yaml', 'r') as file:
    cfg = yaml.safe_load(file)

api = InvenTreeAPI(cfg['SERVER']['URL'], username=cfg['SERVER']['USER'], password=cfg['SERVER']['PWD'])

# GET LOCATIONS
struct = cfg['LOC']['STRUCTURAL']
shlvs = cfg['LOC']['SHELVS']
ig_locs = []
print(struct)
print(shlvs)
print()

# CREATE STRUCTURAL LOCATION
try:
    l = StockLocation.create(api, {
            'structural': True,
            'name': struct['NAME'],
            'description': struct['DESC'],
        }, timeout=1)
except requests.exceptions.HTTPError as e:
            #print(e)
            ig_locs.append(0)
            print(f"Ignored structural location {struct['NAME']}")

# INIT CREATED LOCATIONS LIST
locs = []

# Create main LOCATIONS from YAML
for k, v in shlvs.items():
    d = {}
    #print(k,v)
    if type(v) == list:
        # Add list locations
        locs += v
    elif type(v) == dict:
        # Generate locations
        vt = v['V']
        h = v['H']
        for i in range(vt):
            g = [k+chr(ASCII_START+i)+str(x) for x in range(1, h+1)]
            locs += g

# Create locations
for loc in locs:
    try:
        l = StockLocation.create(api, {
            'structural': False,
            'name': loc,
            'description': '',
        }, timeout=1)
        print(f"Generated location {l.name}")
    except requests.exceptions.HTTPError as e:
        #print(e)
        ig_locs.append(0)
        print(f"Ignored location {loc}")

print("LOCATIONS")
print(locs)


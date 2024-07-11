
#docker compose run --rm inventree-server invoke delete-data
#docker compose run --rm inventree-server invoke setup-test -i

from inventree.api import InvenTreeAPI
from inventree.part import PartCategory
import yaml

with open('_Categories.yaml', 'r') as file:
    cfg = yaml.safe_load(file)

api = InvenTreeAPI(cfg['SERVER']['URL'], username=cfg['SERVER']['USER'], password=cfg['SERVER']['PWD'])

categoriesList = PartCategory.list(api)


nCategories = len(categoriesList)
if nCategories > 0:
    print("DELETING ALL CATEGORIES")
    for cat in categoriesList:
      print(f"Deleting category {cat.name}, PK {cat.pk}")
      cat.delete()
else:
    print("NO CATEGORIES")
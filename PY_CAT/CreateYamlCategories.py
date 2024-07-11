from inventree.api import InvenTreeAPI
from inventree.part import PartCategory
import yaml, requests

ASCII_START = 65

with open('_Categories.yaml', 'r') as file:
    cfg = yaml.safe_load(file)

api = InvenTreeAPI(cfg['SERVER']['URL'], username=cfg['SERVER']['USER'], password=cfg['SERVER']['PWD'])

# GET CATEGORIES
all = cfg['CAT']
print(all)
print()

# INIT CREATED CATEGORIES LIST
all_c = []
ig_cats = []
l1_cat_ns = []
l1_cat_pks = []
l1_cat_ps = []

#print(cat)
#print(type(cat))

# Create main categories from YAML
for k, v in all.items():
    d = {}
    if "DESC" in all[k]:
        d["description"] = all[k]["DESC"]
    if k != "DESC":
        try:
            c = PartCategory.create(api, {
                'parent': None,
                'name': k,
                'description': d['description'],
            }, timeout=1)
            all_c.append(c)
            l1_cat_ns.append(c.name)
            l1_cat_pks.append(c.pk)
            l1_cat_ps.append(c.parent)
        except requests.exceptions.HTTPError as e:
            print(e)
            ig_cats.append(k)


print(f"Created [{len(all_c)}] MAIN CATEGORIES")
#print(f"{all_c}")
print("NAMES", l1_cat_ns)
print("PK", l1_cat_pks)
print("PARENT", l1_cat_ps)
print()



# Get child categories from YAML
l2_cat_ns = []
l2_cat_pks = []
l2_cat_ps = []
for cat in l1_cat_ns:
    for k, v in all[cat].items():
        d = {}
        if "DESC" in all[cat][k]:
            d["description"] = all[cat][k]["DESC"]
        if k != "DESC":
            try:
                c = PartCategory.create(api, {
                    'parent': l1_cat_pks[l1_cat_ns.index(cat)],
                    'name': k,
                    'description': d['description'],
                }, timeout=1)
                all_c.append(c)
                l2_cat_ns.append(c.name)
                l2_cat_pks.append(c.pk)
                l2_cat_ps.append(c.parent)
            except requests.exceptions.HTTPError as e:
                print(e)
                ig_cats.append(k)

print(f"ADDED [{len(l2_cat_ns)}] CHILD CATEGORIES")
#print(f"{all_c}")
print("NAMES", l2_cat_ns)
print("PK", l2_cat_pks)
print("PARENT", l2_cat_ps)
print()

# Get child categories from YAML
l3_cat_ns = []
l3_cat_pks = []
l3_cat_ps = []
for cat in l1_cat_ns:
    for cat2 in l2_cat_ns:
        if cat2 in all[cat]:
            for k, v in all[cat][cat2].items():
                d = {}
                if "DESC" in all[cat][cat2][k]:
                    d["description"] = all[cat][cat2][k]["DESC"]
                if k != "DESC":
                    try:
                        c = PartCategory.create(api, {
                            'parent': l2_cat_pks[l2_cat_ns.index(cat2)],
                            'name': k,
                            'description': d['description'],
                        }, timeout=1)
                        all_c.append(c)
                        l3_cat_ns.append(c.name)
                        l3_cat_pks.append(c.pk)
                        l3_cat_ps.append(c.parent)
                    except requests.exceptions.HTTPError as e:
                        print(e)
                        ig_cats.append(k)

print(f"ADDED [{len(l3_cat_ns)}] CHILD CATEGORIES")
#print(f"{all_c}")
print("NAMES", l3_cat_ns)
print("PK", l3_cat_pks)
print("PARENT", l3_cat_ps)
print()



print(f"TOTAL {len(l1_cat_ns)+len(l2_cat_ns)+len(l3_cat_ns)} CATEGORIES")
print(f"IGNORED {len(ig_cats)} CATEGORIES")
from inventree.api import InvenTreeAPI
from inventree.stock import StockLocation

SERVER_ADDRESS = 'http://192.168.31.100:8000'
MY_USERNAME = 'USER'
MY_PASSWORD = 'PASSWORD'

api = InvenTreeAPI(SERVER_ADDRESS, username=MY_USERNAME, password=MY_PASSWORD)

#####GrandParents
nShelvs = 11
firstGrandParent = 65 #A
grandParentsList = []
for idx in range(nShelvs):
  name = chr(firstGrandParent+idx)
  print("Creating GrandParent ", name)
  grandParent = StockLocation.create(api, {'name':name,'description':'','parent':''})
  grandParentsList.append(grandParent)
#print("grandParentsList:", grandParentsList)
nGrandParents = len(grandParentsList)
print("Number of grandParents:", nGrandParents)
for idx in range(nGrandParents):
  print("GrandParent number", idx, " is ", grandParentsList[idx].pk)

#####Parents
nLevels = 2
firstParent = 97 #a
parentsList = []
for idx in range(nGrandParents):
  for iidx in range(nLevels):
    print("Creating Parent ", name, " from GrandParent ", grandParentsList[idx].pk)
    name = chr(firstGrandParent+idx)+chr(firstParent+iidx)
    parent = StockLocation.create(api, {'name':name,'description':'','parent':grandParentsList[idx].pk})
    parentsList.append(parent)
#print("parentsList:", parentsList)
nParents = len(parentsList)
print("Number of parents:", nParents)
for idx in range(nParents):
  print("Parent number", idx, " is ", parentsList[idx].pk)

#####Childs
nChilds = 5
offsetChilds = 1
childList = []
for idx in range(nParents):
  for iidx in range(nChilds):
    print("Creating Child ", name, " from Parent ", parentsList[idx].pk)
    name = chr(firstGrandParent+idx)+chr(firstParent+iidx)+str(iidx+offsetChilds)
    child = StockLocation.create(api, {'name':name,'description':'','parent':parentsList[idx].pk})
    childList.append(child)
#print("childList:", childList)
nSubChilds = len(childList)
print("Number of childs:", nSubChilds)
for idx in range(nSubChilds):
  print("Child number", idx, " is ", childList[idx].pk)
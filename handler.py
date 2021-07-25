import pymongo
import os

MONGODB_URL = os.environ['MONGODB_URL']
MONGODB_DB = os.environ["MONGODB_DB"]
MONGODB_COL = os.environ["MONGODB_COL"]
INSERT_ROWS = 10000

client = pymongo.MongoClient(MONGODB_URL)

def reader(event, context):
  db = client[MONGODB_DB]
  testCol = db[MONGODB_COL]

  cursor = testCol.find({})
  rowCount = 0
  for row in cursor:
    rowCount += 1
    print(row)

  print('Total rows retrieved {}'.format(rowCount))  

def writer(event, context):
  db = client[MONGODB_DB]
  testCol = db[MONGODB_COL]

  rowCount = 0
  for rowNum in range(INSERT_ROWS):      
    testCol.insert_one({"rowNum": rowNum, "firstName": "Dhaval", "lastName": "Nagar"})  
    rowCount += 1

  print('Total rows written {}'.format(rowCount))
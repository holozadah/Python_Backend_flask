conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.store_inventory


db.produce.insert_many(
    [
        {
      "type": "apples",
      "cost": .23,
      "stock": 333
  }
    ]
)
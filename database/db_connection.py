from pymongo import MongoClient  

#Establish connection with MongoDB and return the database object.
def get_db():
    client = MongoClient("mongodb://localhost:27017")
    db = client["log_aggregator"]
    return db

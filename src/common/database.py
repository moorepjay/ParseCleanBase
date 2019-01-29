import pandas as pd

import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['parse']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def dump_to_csv(path):
        get_db = Database.find("parseTest", {})
        df = pd.DataFrame(list(get_db))
        df.to_csv(path)

    # @staticmethod
    # def update_entry(collection, request_id):
    #     return Database.DATABASE[collection].update_one({"Request ID": request_id},
    #                                                     { $set: {"Comments": }})

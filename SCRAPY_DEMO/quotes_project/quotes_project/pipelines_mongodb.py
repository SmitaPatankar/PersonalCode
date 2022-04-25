# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter

class QuotesProjectPipeline:
    def __init__(self):
        self.create_connection()
        self.create_db_table()

    def create_connection(self):
        self.conn = pymongo.MongoClient(
            "localhost",
            "portnumberinint")

    def create_db_table(self):
        db  = self.conn["quotes_db"]
        self.collection = db["quotes"]

    def store_db(self, item):
        pass

    def process_item(self, item, spider):
        self.collection.insert(dict(item))

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
from itemadapter import ItemAdapter

class QuotesProjectPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="concealed",
            password="concealed",
            database="quotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        query = """drop table if exists quotes"""
        self.curr.execute(query)

        query = """create table quotes(
            title text,
            author text,
            tag text
        )"""
        self.curr.execute(query)

    def store_db(self, item):
        self.curr.execute(
            """insert into quotes values(%s,%s,%s)""",
            (item["title"][0], item["author"][0], item["tag"][0]))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

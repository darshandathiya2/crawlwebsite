# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import _sqlite3


class CrawlwebsitePipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = _sqlite3.connect("mycrawlwebsite.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS crawlwebsite_tb""")
        self.curr.execute(""" create table crawlwebsite_tb(
                    actor_name text,
                    personality varchar,
                   actor_image varchar

                      )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into crawlwebsite_tb values (?,?,?)""", (
            item['actor_name'][0],
            item['personality'][0],
            item['actor_image'][0]
        ))
        self.conn.commit()



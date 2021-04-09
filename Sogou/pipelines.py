# encoding=utf-8
import pymongo
from Sogou.items import SogouItem


class MongoDBPipleline(object):
    def __init__(self):
        client = pymongo.MongoClient("8.131.55.73", 27017)
        db = client["Sina"]
        try:
            db.authenticate("along", "123456al")
        except:
            print("mongodb链接失败")
        self.Sogou = db["Sogou"]

    def process_item(self, item, spider):
        try:
            self.Sogou.insert(dict(item))
        except Exception:
            pass
        return item

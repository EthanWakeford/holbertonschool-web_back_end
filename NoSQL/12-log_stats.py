#!/usr/bin/env python3
"""logs stats"""
from pymongo import MongoClient


def loggedStats():
    """logs the stats"""
    client = MongoClient()
    db = client.logs
    coll = db.nginx
    print("{} logs".format(coll.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"\tmethod {method}: " +
              f"{coll.count_documents({'method': method})}")
    print(f"{coll.count_documents({'method': 'GET', 'path': '/status'})} \
status check")


if __name__ == "__main__":
    loggedStats()

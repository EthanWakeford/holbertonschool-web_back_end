#!/usr/bin/env python3
"""updates stuff"""

def update_topics(mongo_collection, name, topics):
    """updates the topics"""
    return mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

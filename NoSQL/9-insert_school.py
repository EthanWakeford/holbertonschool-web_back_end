#!/usr/bin/env python3
"""inserts into collections"""


def insert_school(mongo_collection, **kwargs):
    """inserts into collection"""
    post = {**kwargs}
    post_id = mongo_collection.insert_one(post).inserted_id
    return post_id

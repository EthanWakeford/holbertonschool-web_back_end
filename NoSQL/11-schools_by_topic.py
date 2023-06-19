#!/usr/bin/env python3
"""returns schools based on topic"""


def schools_by_topic(mongo_collection, topic):
    """returns schools by topic"""
    return mongo_collection.find({'topics': topic})

#!/usr/bin/env python3
"""list all mongo docs"""


def list_all(mongo_collection):
    """lists all """
    return mongo_collection.find()

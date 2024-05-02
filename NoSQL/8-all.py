#!/usr/bin/python3
"""list all doc in a collection"""


def list_all(mongo_collection):
    """return mongo_collection"""
    return mongo_collection.find()

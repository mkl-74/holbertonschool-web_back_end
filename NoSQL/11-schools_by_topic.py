#!/usr/bin/env python3
"""Return a schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """Return schools by topic"""
    schools = mongo_collection.find({"topics": topic})
    return [school for school in schools]

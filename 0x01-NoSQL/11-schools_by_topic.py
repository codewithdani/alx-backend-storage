#!/usr/bin/env python3
"""
Find documents in the collection with the specified topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Find documents in the collection with the specified topic
    """
    return mongo_collection.find({"topics": topic})

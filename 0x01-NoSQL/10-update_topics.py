#!/usr/bin/env python3
"""
update school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update documents with the specified school name
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

#!/usr/bin/env python3
"""
Import the pymongo library for interacting with MongoDB.
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document
    """
    result = mongo_collection.insert_one(kwargs)
    
    # Return the new _id
    return result.inserted_id

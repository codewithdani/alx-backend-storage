#!/usr/bin/env python3
"""
Import the pymongo library for interacting with MongoDB.
"""
import pymongo


def list_all(mongo_collection):
    """
    Find all documents in the collection
    """
    documents = mongo_collection.find()
    return list(documents)

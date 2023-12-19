#!/usr/bin/env python3
"""
Display the total number of logs
"""
from pymongo import MongoClient


def print_nginx_logs_stats(mongo_collection):
   """  Display the total number of logs """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs where {total_logs} is the number of documents in this collection")

   """  Display the count of logs for each HTTP method """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\t{count} logs with method={method}")

    """ Display the count of logs with method=GET and path=/status """
    special_log_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{special_log_count} logs with method=GET and path=/status")





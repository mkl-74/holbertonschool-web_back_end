#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient

def nginx_stats():
    """Récupère des statistiques sur les logs Nginx depuis MongoDB"""
    client = MongoClient()
    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_checks = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")

if __name__ == "__main__":
    nginx_stats()
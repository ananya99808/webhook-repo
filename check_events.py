from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webhook_db"]
collection = db["events"]

print("🔍 All events in MongoDB:\n")
for event in collection.find().sort("timestamp", -1):
    print("Event Type:", event.get("event_type"))
    print("Action:", event.get("payload", {}).get("action"))
    if event.get("event_type") == "pull_request":
        merged = event.get("payload", {}).get("pull_request", {}).get("merged", False)
        print("Merged:", merged)
    print("Timestamp:", event.get("timestamp"))
    print("-" * 40)

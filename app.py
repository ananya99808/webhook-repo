from flask import Flask, request, jsonify, render_template  
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["webhook_db"]
collection = db["events"]

@app.route("/webhook", methods=["POST"])
def webhook():
    # (your existing code here)
    ...
    return jsonify({"status": "success"}), 200

# ✅ ADD THIS BELOW YOUR /webhook ROUTE

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/events")
def get_events():
    events = list(collection.find().sort("timestamp", -1).limit(10))
    for event in events:
        event["_id"] = str(event["_id"])
        event["timestamp"] = event["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        event["action"] = event.get("payload", {}).get("action", None)
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug=True)

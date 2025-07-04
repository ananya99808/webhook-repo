from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["github_events"]
collection = db["events"]

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        event_type = request.headers.get("X-GitHub-Event", "unknown")

        if event_type == "push":
            repo_name = data.get("repository", {}).get("full_name")
            pusher = data.get("pusher", {}).get("name")
            timestamp = datetime.utcnow()

            collection.insert_one({
                "event_type": event_type,
                "repo": repo_name,
                "pusher": pusher,
                "timestamp": timestamp,
                "payload": data
            })

            return jsonify({"status": "Push event received"}), 200
        else:
            return jsonify({"status": "Unhandled event type"}), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": "Something went wrong"}), 400

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from datetime import datetime, timedelta


app = Flask(__name__)

@app.route("/api", methods=["GET"])
def create_endpoint():
    """GET request query parameter that get the slack name and track"""
    track = request.args.get("track")
    slack_name = request.args.get("slack_name")

    """Get the current day of the week"""
    current_day = datetime.now().strftime("%A")

    """Get the current UTC time"""
    current_time = (datetime.utcnow() + timedelta(minutes=2)).isoformat()

    """Get the GitHub URL """
    github_file_url = "https://github.com/chykB/hng_projects/tree/main/endpoint_task"

    """Get the github repo url"""
    github_repo = "https://github.com/chykB/hng_projects"

    """Return response in json format"""
    response_data={
        "track": track,
        "slack_name": slack_name,
        "current_day": current_day,
        "current_time": current_time,
        "github_file_url": github_file_url,
        "github_repo": github_repo,
        "status_code": 200
    }
    return jsonify(response_data)
if __name__ == "__main__":
    app.run(debug=True)
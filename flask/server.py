from flask import Flask, request, jsonify
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define the file path
file_path = r"/storage/emulated/0/tiranga/tir/flask/11_aug.json"

# Function to sort data by issueNumber and remove duplicates
def setup_data(data):
    # Sort the data by issueNumber in descending order
    data_sorted = sorted(data, key=lambda x: x["issueNumber"], reverse=True)

    # Remove duplicate issueNumbers while keeping the highest (most recent) entry
    unique_data = []
    seen_issues = set()
    for entry in data_sorted:
        if entry["issueNumber"] not in seen_issues:
            unique_data.append(entry)
            seen_issues.add(entry["issueNumber"])

    return unique_data

@app.route('/save_data', methods=['POST'])
def save_data():
    new_data = request.json
    if new_data:
        # Load existing data from the JSON file if it exists
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        # Combine existing data with new data
        combined_data = new_data + existing_data

        # Process the combined data to sort and remove duplicates
        processed_data = setup_data(combined_data)

        # Write the result back to the JSON file in a systematic and readable format
        with open(file_path, 'w') as file:
            json.dump(processed_data, file, indent=4, sort_keys=True)

        return jsonify({"status": "success", "message": "Data saved and sorted successfully"}), 200
    else:
        return jsonify({"status": "failure", "message": "No data provided"}), 400

if __name__ == '__main__':
    port = int(input("Enter the port number to run the Flask application: "))
    app.run(debug=True, port=port)

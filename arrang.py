import json

# Define the file path
file_path = r"E:\Gopal\tir\data_request.json"

# Load data from the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Sort the data by issueNumber in descending order
data_sorted = sorted(data, key=lambda x: x["issueNumber"], reverse=True)

# Remove duplicate issueNumbers
unique_data = []
seen_issues = set()
for entry in data_sorted:
    if entry["issueNumber"] not in seen_issues:
        unique_data.append(entry)
        seen_issues.add(entry["issueNumber"])

# Write the result back to the same JSON file
with open(file_path, 'w') as file:
    json.dump(unique_data, file, indent=4)

print(f"Data has been sorted and updated in {file_path}")

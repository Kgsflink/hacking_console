from flask import Flask, render_template_string, request
import json
from collections import defaultdict

app = Flask(__name__)

def get_color(number):
    if int(number) in [0, 2, 4, 6, 8]:
        return 'red'
    else:
        return 'green'

def get_size(number):
    if int(number) in [0, 1, 2, 3, 4]:
        return 'small'
    else:
        return 'big'

def find_sequences(data, min_length=4, pattern_check=None):
    sequences = []
    current_sequence = []
    
    for i in range(len(data)):
        number = data[i]["number"]
        color = get_color(number)
        size = get_size(number)
        
        if pattern_check:
            if i == 0 or pattern_check(data, i):
                current_sequence.append(data[i])
            else:
                if len(current_sequence) >= min_length:
                    sequences.append(current_sequence)
                current_sequence = [data[i]]
        else:
            if i == 0 or (color == get_color(data[i-1]["number"]) and size == get_size(data[i-1]["number"])):
                current_sequence.append(data[i])
            else:
                if len(current_sequence) >= min_length:
                    sequences.append(current_sequence)
                current_sequence = [data[i]]
    
    if len(current_sequence) >= min_length:
        sequences.append(current_sequence)
    
    return sequences

def big_small_pattern(data, i):
    number = data[i]["number"]
    size = get_size(number)
    return size != get_size(data[i-1]["number"])

def format_output(sequences, trend_description):
    output = []
    for seq in sequences:
        start = seq[0]["issueNumber"]
        end = seq[-1]["issueNumber"]
        start_time = issue_number_to_time(start)
        output.append([trend_description, start, end, start_time, len(seq)])
    return output

def issue_number_to_time(issue_number):
    last_four_digits = int(issue_number[-4:])
    hours = last_four_digits // 60
    minutes = last_four_digits % 60
    return f"{hours:02}:{minutes:02}"

def filter_data_by_issue_number(data, initial_issue_number):
    return [entry for entry in data if entry["issueNumber"] >= initial_issue_number]

def group_by_hour(data):
    hourly_groups = defaultdict(list)
    for entry in data:
        issue_number = entry["issueNumber"]
        hour = issue_number_to_time(issue_number)[:2]  # Get only the hour part
        hourly_groups[hour].append(entry)
    return hourly_groups

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []
    initial_issue_number = ""

    if request.method == 'POST':
        initial_issue_number = request.form['issueNumber']
        
        with open('/storage/emulated/0/Download/collected_data_1723705075430.json', 'r') as file:
            data = json.load(file)
        
        data.sort(key=lambda x: x['issueNumber'])
        filtered_data = filter_data_by_issue_number(data, initial_issue_number)
        hourly_data = group_by_hour(filtered_data)
        
        combined_output = []
        for hour, entries in hourly_data.items():
            red_sequences = find_sequences(entries, pattern_check=lambda d, i: get_color(d[i]["number"]) == 'red')
            green_sequences = find_sequences(entries, pattern_check=lambda d, i: get_color(d[i]["number"]) == 'green')
            big_sequences = find_sequences(entries, pattern_check=lambda d, i: get_size(d[i]["number"]) == 'big')
            small_sequences = find_sequences(entries, pattern_check=lambda d, i: get_size(d[i]["number"]) == 'small')
            big_small_sequences = find_sequences(entries, pattern_check=big_small_pattern)

            red_output = format_output(red_sequences, "Red Trend")
            green_output = format_output(green_sequences, "Green Trend")
            big_output = format_output(big_sequences, "Big Trend")
            small_output = format_output(small_sequences, "Small Trend")
            big_small_output = format_output(big_small_sequences, "Big-Small Pattern")

            max_length = max(len(red_output), len(green_output), len(big_output), len(small_output), len(big_small_output))

            for i in range(max_length):
                row = [hour]
                row.extend(red_output[i] if i < len(red_output) else ["Red Trend", "", "", "", ""])
                row.extend(green_output[i] if i < len(green_output) else ["Green Trend", "", "", "", ""])
                row.extend(big_output[i] if i < len(big_output) else ["Big Trend", "", "", "", ""])
                row.extend(small_output[i] if i < len(small_output) else ["Small Trend", "", "", "", ""])
                row.extend(big_small_output[i] if i < len(big_small_output) else ["Big-Small Pattern", "", "", "", ""])
                combined_output.append(row)
        
        return render_template_string(template, combined_output=combined_output, headers=headers, initial_issue_number=initial_issue_number)

    return render_template_string(template, combined_output=[], headers=headers, initial_issue_number=initial_issue_number)

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trend Data</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }
        th { background-color: #f2f2f2; }
        form { margin: 20px 0; }
    </style>
</head>
<body>
    <h1>Trend Data</h1>
    <form method="post">
        <label for="issueNumber">Enter Initial Issue Number:</label>
        <input type="text" id="issueNumber" name="issueNumber" value="{{ initial_issue_number }}" required>
        <button type="submit">Submit</button>
    </form>
    <table>
        <thead>
            <tr>
                <th>Hour</th>
                {% for header in headers %}
                    <th>{{ header }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for row in combined_output %}
                <tr>
                    {% for cell in row %}
                        <td>{{ cell }}</td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

headers = ["Hour",
           "Trend", "Start IssueNumber", "End IssueNumber", "Start Time", "Length",
           "Trend", "Start IssueNumber", "End IssueNumber", "Start Time", "Length",
           "Trend", "Start IssueNumber", "End IssueNumber", "Start Time", "Length",
           "Trend", "Start IssueNumber", "End IssueNumber", "Start Time", "Length",
           "Trend", "Start IssueNumber", "End IssueNumber", "Start Time", "Length"]

if __name__ == '__main__':
    app.run(debug=True)

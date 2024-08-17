import json
from tabulate import tabulate

# Load data from the JSON file
with open('28_jul.json', 'r') as file:
    data = json.load(file)

# Sort the data by 'issueNumber' in increasing order
data.sort(key=lambda x: x['issueNumber'])

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

def define_trend_name(color, size):
    if color == 'red' and size == 'small':
        return 'Red Small'
    elif color == 'red' and size == 'big':
        return 'Red Big'
    elif color == 'green' and size == 'small':
        return 'Green Small'
    elif color == 'green' and size == 'big':
        return 'Green Big'

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
        output.append([trend_description, start, end, len(seq)])
    return output

def filter_data_by_issue_number(data, initial_issue_number):
    return [entry for entry in data if entry["issueNumber"] >= initial_issue_number]

# Ask for the initial issueNumber
initial_issue_number = input("Enter the initial issueNumber to start finding results: ")

# Filter the data based on the initial issueNumber
filtered_data = filter_data_by_issue_number(data, initial_issue_number)

# Find and format sequences for each trend
color_sequences = find_sequences(filtered_data)
big_sequences = find_sequences(filtered_data, pattern_check=lambda d, i: get_size(d[i]["number"]) == 'big')
small_sequences = find_sequences(filtered_data, pattern_check=lambda d, i: get_size(d[i]["number"]) == 'small')
big_small_sequences = find_sequences(filtered_data, pattern_check=big_small_pattern)

# Prepare output for each trend
output = []
output.extend(format_output(color_sequences, "Color Trend"))
output.extend(format_output(big_sequences, "Big Trend"))
output.extend(format_output(small_sequences, "Small Trend"))
output.extend(format_output(big_small_sequences, "Big-Small Pattern"))

# Print the table
print(tabulate(output, headers=["Trend", "Start IssueNumber", "End IssueNumber", "Length"]))

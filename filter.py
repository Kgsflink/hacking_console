import json
from tabulate import tabulate

def load_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def find_sequences(data, num_values):
    num_values = list(num_values)  # Convert to list to maintain order
    num_count = len(num_values)

    # Sort data by 'round' in ascending order
    sorted_data = sorted(data, key=lambda x: x['round'])

    matches = []
    for i in range(len(sorted_data) - num_count + 1):
        sequence_matches = all(
            sorted_data[i + j]['num'] == num_values[j]
            for j in range(num_count)
        )
        if sequence_matches:
            start_range = max(i - 1, 0)
            end_range = min(i + num_count + 3, len(sorted_data))
            results = sorted_data[start_range:end_range]
            matches.append(results)

    return matches

def print_matches(matches):
    for match in matches:
        headers = match[0].keys()
        rows = [x.values() for x in match]
        print(tabulate(rows, headers, tablefmt='grid'))
        print("\n")

# File path to the JSON data
file_path = '19_dbs.json'

# Load data from the JSON file
data = load_data_from_file(file_path)

# Example usage
num_input = input("Enter num values separated by spaces: ")
num_values = num_input.split()

matches = find_sequences(data, num_values)

print("Filtered Results:")
if matches:
    print_matches(matches)
else:
    print("No matches found.")

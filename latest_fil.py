import json
from tabulate import tabulate

def load_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def find_sequences(data, num_values):
    num_values = list(num_values)  # Convert to list to maintain order
    num_count = len(num_values)

    # Convert 'issueNumber' values to integers for proper sorting
    for item in data:
        item['issueNumber'] = int(item['issueNumber'])

    # Sort data by 'issueNumber' in ascending order
    sorted_data = sorted(data, key=lambda x: x['issueNumber'])

    matches = []
    for i in range(len(sorted_data) - num_count + 1):
        sequence_matches = all(
            sorted_data[i + j]['number'] == num_values[j]
            for j in range(num_count)
        )
        if sequence_matches:
            start_range = max(i - 3, 0)
            end_range = min(i + num_count + 10, len(sorted_data))
            results = sorted_data[start_range:end_range]
            matches.append(results)

    return matches

def find_color_trend_sequences(data, pattern):
    # Convert 'issueNumber' values to integers for proper sorting
    for item in data:
        item['issueNumber'] = int(item['issueNumber'])

    # Sort data by 'issueNumber' in ascending order
    sorted_data = sorted(data, key=lambda x: x['issueNumber'])

    pattern_length = len(pattern)
    matches = []
    for i in range(len(sorted_data) - pattern_length + 1):
        trend_matches = all(
            sorted_data[i + j]['colour'] == pattern[j]
            for j in range(pattern_length)
        )
        if trend_matches:
            start_range = max(i - 1, 0)
            end_range = min(i + pattern_length + 3, len(sorted_data))
            results = sorted_data[start_range:end_range]
            matches.append(results)

    return matches

def find_size_trend_sequences(data, size_sequence):
    size_sequence = list(size_sequence)  # Convert to list to maintain order
    size_sequence_length = len(size_sequence)

    # Convert 'issueNumber' values to integers for proper sorting
    for item in data:
        item['issueNumber'] = int(item['issueNumber'])

    # Sort data by 'issueNumber' in ascending order
    sorted_data = sorted(data, key=lambda x: x['issueNumber'])

    def is_size_match(number, size):
        number = int(number)  # Convert number to integer
        if size == 'big':
            return 5 <= number <= 9
        elif size == 'small':
            return 0 <= number <= 4
        return False

    matches = []
    for i in range(len(sorted_data) - size_sequence_length + 1):
        size_matches = all(
            is_size_match(sorted_data[i + j]['number'], size_sequence[j])
            for j in range(size_sequence_length)
        )
        if size_matches:
            start_range = max(i - 1, 0)
            end_range = min(i + size_sequence_length + 3, len(sorted_data))
            results = sorted_data[start_range:end_range]
            matches.append(results)

    return matches

def print_matches(matches):
    for match in matches[::-1]:  # Print the latest trends first
        headers = match[0].keys()
        rows = [x.values() for x in match]
        print(tabulate(rows, headers, tablefmt='grid'))
        print("\n")

# File path to the JSON data
file_path = 'data_request.json'

# Load data from the JSON file
data = load_data_from_file(file_path)

# Main functionality
while True:
    choice = input("Choose an option:\n1. Find sequences by 'number' values\n2. Find continuous color trends\n3. Find continuous size trends\nEnter your choice (1, 2, or 3): ")

    if choice == '1':
        num_input = input("Enter 'number' values separated by spaces: ")
        num_values = num_input.split()
        matches = find_sequences(data, num_values)
        print("Filtered Results:")
        if matches:
            print_matches(matches)
        else:
            print("No matches found.")
    elif choice == '2':
        pattern_input = input("Enter color pattern (e.g., green green red red green): ")
        pattern = pattern_input.split()
        matches = find_color_trend_sequences(data, pattern)
        print("Filtered Results:")
        if matches:
            print_matches(matches)
        else:
            print("No matches found.")
    elif choice == '3':
        size_sequence_input = input("Enter size sequence (e.g., big small big): ")
        size_sequence = size_sequence_input.split()
        matches = find_size_trend_sequences(data, size_sequence)
        print("Filtered Results:")
        if matches:
            print_matches(matches)
        else:
            print("No matches found.")
    else:
        print("Invalid choice. Please try again.")

    cont = input("Do you want to continue? (yes or no): ").strip().lower()
    if cont != 'yes':
        break

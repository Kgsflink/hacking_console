import json

def sum_of_digits(number):
    """Calculate the sum of the digits of a number."""
    return sum(int(digit) for digit in str(number))

def get_premium_data(data, start_issue, end_issue):
    """Calculate the total sum of the premium digit sum and the average premium for a given range of issueNumbers."""
    total_digit_sum = 0
    total_premium = 0
    count = 0
    
    for item in data:
        if start_issue <= item['issueNumber'] <= end_issue:
            premium = int(item['premium'])  # Ensure premium is an integer
            premium_digit_sum = sum_of_digits(premium)
            total_digit_sum += premium_digit_sum
            total_premium += premium
            count += 1
            
    average_premium = total_premium / count if count > 0 else 0
    return total_digit_sum, average_premium

def display_table(data, start_issue, end_issue, sum_premium, avg_premium):
    """Display the extracted data in a table format."""
    print("+------------------+--------+--------------+---------+-------------------+")
    print("|  Issue Number    | Number |    Colour    | Premium | Premium Digit Sum |")
    print("+------------------+--------+--------------+---------+-------------------+")
    
    for item in data:
        if start_issue <= item['issueNumber'] <= end_issue:
            premium = int(item['premium'])  # Ensure premium is an integer
            premium_digit_sum = sum_of_digits(premium)
            print(f"| {item['issueNumber']} |   {item['number']}    | {item['colour']} | {premium}  |        {premium_digit_sum}        |")
    
    print("+------------------+--------+--------------+---------+-------------------+")
    print(f"\nTotal Premium Digit Sum from {start_issue} to {end_issue}: {sum_premium}")
    print(f"Average Premium from {start_issue} to {end_issue}: {avg_premium:.2f}")

def calculate_average_for_last_n_rounds(data, n):
    """Calculate the average of the premium digit sums and premium numbers for the last n rounds."""
    premiums = [sum_of_digits(int(item['premium'])) for item in data[-n:]]
    premium_numbers = [int(item['premium']) for item in data[-n:]]
    
    avg_digit_sum = sum(premiums) / len(premiums) if premiums else 0
    avg_premium = sum(premium_numbers) / len(premium_numbers) if premium_numbers else 0
    
    return avg_digit_sum, avg_premium

def predict_next(data):
    """Predict the next period result based on averages of the last 10, 20, 30, 50, and 100 rounds."""
    last_10_avg, last_10_premium_avg = calculate_average_for_last_n_rounds(data, 10)
    last_20_avg, last_20_premium_avg = calculate_average_for_last_n_rounds(data, 20)
    last_30_avg, last_30_premium_avg = calculate_average_for_last_n_rounds(data, 30)
    last_50_avg, last_50_premium_avg = calculate_average_for_last_n_rounds(data, 50)
    last_100_avg, last_100_premium_avg = calculate_average_for_last_n_rounds(data, 100)
    
    print("\nPredicted next period result:")
    print("+------------------+--------+-------------------------------------------+")
    print("|   Next Number    | Premium Digit Sum (Averages) | Premium Avg (Averages) |")
    print("+------------------+--------+-------------------------------------------+")
    print(f"|       ?        |    Last 10: {round(last_10_avg)}    |    Last 10: {round(last_10_premium_avg, 2)}    |")
    print(f"|       ?        |    Last 20: {round(last_20_avg)}    |    Last 20: {round(last_20_premium_avg, 2)}    |")
    print(f"|       ?        |    Last 30: {round(last_30_avg)}    |    Last 30: {round(last_30_premium_avg, 2)}    |")
    print(f"|       ?        |    Last 50: {round(last_50_avg)}    |    Last 50: {round(last_50_premium_avg, 2)}    |")
    print(f"|       ?        |    Last 100: {round(last_100_avg)}   |    Last 100: {round(last_100_premium_avg, 2)}   |")
    print("+------------------+--------+-------------------------------------------+")

def calculate_digit_probability(data, rounds):
    """Calculate the probability of each digit (0-9) appearing in the premium numbers for the last n rounds."""
    digit_counts = [0] * 10
    premium_digits = [str(item['premium']) for item in data[-rounds:]]

    for premium in premium_digits:
        for digit in premium:
            digit_counts[int(digit)] += 1

    total_digits = rounds * len(str(data[0]['premium']))
    probabilities = [count / total_digits for count in digit_counts]

    return probabilities

def main():
    file_path = "/storage/emulated/0/Download/collected_data_1723705075430.json"
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error reading JSON data.")
        return
    
    # Remove duplicate entries based on issueNumber and sort by issueNumber
    unique_data = {item['issueNumber']: item for item in data}.values()
    sorted_data = sorted(unique_data, key=lambda x: x['issueNumber'])
    
    start_issue = sorted_data[0]['issueNumber']
    end_issue = sorted_data[-1]['issueNumber']
    
    sum_premium, avg_premium = get_premium_data(sorted_data, start_issue, end_issue)
    display_table(sorted_data, start_issue, end_issue, sum_premium, avg_premium)
    predict_next(sorted_data)

    rounds = [10, 20, 30, 50, 100]
    for round in rounds:
        probabilities = calculate_digit_probability(sorted_data, round)
        print(f"\nDigit probabilities for last {round} rounds:")
        print("+--------+------------+")
        print("| Digit  | Probability|")
        print("+--------+------------+")
        for i, prob in enumerate(probabilities):
            print(f"|   {i}    |   {prob:.4f}   |")
        print("+--------+------------+")

if __name__ == "__main__":
    main()

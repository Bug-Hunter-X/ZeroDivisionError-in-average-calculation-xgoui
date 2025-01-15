def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage that causes the error
data = []
average = calculate_average(data)
print(f"The average is: {average}")
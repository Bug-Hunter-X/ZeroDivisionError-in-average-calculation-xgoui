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

#Robust solution
def calculate_average_robust(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
data = []
average = calculate_average_robust(data)
print(f"The robust average is: {average}")

data = [10,20,30]
average = calculate_average_robust(data)
print(f"The robust average is: {average}")

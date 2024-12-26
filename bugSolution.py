def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

#Improved Version
def calculate_average_improved(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
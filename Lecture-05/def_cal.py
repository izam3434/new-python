def calculate_stats(numbers):
    total_sum   = sum(numbers)
    average = total_sum / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total_sum, average, minimum, maximum

numbers = [5, 10, 15, 20, 25]
total_sum, average, minimum, maximum = calculate_stats(numbers)

print(f"Total Sum: {total_sum}")
print(f"Average: {average}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
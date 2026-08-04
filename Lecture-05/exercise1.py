def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    return armstrong_sum == number
print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))
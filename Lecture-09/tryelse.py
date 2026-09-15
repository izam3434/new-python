try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("Cannot divide By zero!")
else:
    print(f"The result is {result}")
print("End of program")
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input! Plase enter a number")
except ZeroDivisionError:
    print("Cannot divide by Zero!")

print("End of Program")
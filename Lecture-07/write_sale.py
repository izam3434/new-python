num_days = int(input("for how many days do you want to enter sales?: "))
with open("sales.txt", "w") as sales_file:
    for count in range(1, num_days + 1):
        sales = float(input(f"Enter the sales for day {count}: "))
        sales_file.write(str(sales) + "\n")

print("Sales data has been written to sales.txt.")
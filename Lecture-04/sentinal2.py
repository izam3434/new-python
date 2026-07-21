rows = input("Enter the number of rows: ")
columns = input("Enter the number of columns: ")
for i in range(int(rows)):
    for j in range(int(columns)):
        print("*", end="")
    print()
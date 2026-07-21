numbers = int(input("Enter the number : "))
for i in range(1, 101):
    print(f"{i:>3}", end=" ")
    if i % numbers == 0:
        print()
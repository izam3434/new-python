keep_going = 'y'
while keep_going == 'y':
    whc = float(input("Enter the item wholesale cost: "))
    rtp = whc * 2.5
    print(f"the retail price is: {rtp:.2f}")
    keep_going = input("Do you want to calculate another " + " retail price? (Enter y for yes): ")
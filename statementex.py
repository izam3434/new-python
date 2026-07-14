test1 = int(input("Enter your score test 1: "))
test2 = int(input("Enter your score test 2: "))
test3 = int(input("Enter your score test 3: "))
sum = test1 + test2 + test3
average = sum / 3
print("Your average score is: " + format(average, ".2f"))
if average > 95:
    print("Congratulations!")
elif average < 95:
    print("You need to work harder.")
score = int(input("Enter your score: "))
print("Your score is: " + format(score, ".2f"))
if score >= 50:
    print("Display pass")
else:
    print("Display fail")
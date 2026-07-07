width = input("Enter your width in kilograms: ")
width = float(width)

height = input("Enter your height in meters: ")
height = float(height)

bmi = width / (height ** 2)
print("Your BMI is: " + format(bmi, ".2f"))

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
else:
    print("You are overweight.")
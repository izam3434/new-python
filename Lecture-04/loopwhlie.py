import random
print("What is my magic number (1 to 100) ?")
mynumber = random.randint(1, 100)
ntries = 1
yourguess = -1
while ntries <= 10 and yourguess != mynumber:
    msg = str(ntries) + ">>"
    if(ntries == 1):
        print("You have 10 tries to guess the number")
    yourguess = int(input(msg))
    if yourguess > mynumber:
        print("--> too high")
    elif yourguess < mynumber:
        print("--> too low")
    ntries += 1
if yourguess == mynumber:
    print("You got it in",mynumber)
else:
    print("Sorry, the number was", mynumber)
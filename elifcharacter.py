inchar = input("Enter a character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("You in put is uppercase letter.", inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You in put is lowercase letter.", inchar)
elif inchar >= '0' and inchar <= '9':
    print("You in put number.", inchar)
else:
    print("You in put is a letter or number.", inchar)
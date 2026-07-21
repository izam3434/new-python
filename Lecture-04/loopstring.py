input_string = input("Enter a string: ")
modified_string = ""
vowels = "aeiouAEIOU"
for char in input_string:
    uper_char = char.upper()
    if uper_char in vowels:
        modified_string += "#"
    else:
        modified_string += uper_char
print("Modified string:", modified_string)
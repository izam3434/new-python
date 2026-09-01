with open('example.txt', 'w') as infile:
    lines = infile.readlines()
    while line:
        print(lines.strip())
        line = infile.readline()
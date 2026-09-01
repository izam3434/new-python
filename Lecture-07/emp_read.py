with open("employees.txt", "r") as emp_file:
    for line in emp_file:
        print("name: " + line.strip())
        print("id number: " + emp_file.readline().strip())
        print("department: " + emp_file.readline().strip())
        print()
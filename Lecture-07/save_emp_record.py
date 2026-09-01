num_emps = int(input("for how many employees do you want to enter records?: "))
with open("employees.txt", "w") as emp_file:
    for count in range(1, num_emps + 1):
        print("employee number #", count, sep="")
        name = input("name: ")
        id_number = input("id number: ")
        department = input("department: ")

        emp_file.write(name + "\n")
        emp_file.write(id_number + "\n")
        emp_file.write(department + "\n")
        print()

print("Employee records have been written to employees.txt.")
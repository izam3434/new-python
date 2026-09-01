import struct

num_records = int(input("Enter the number of records to write: "))
with open('records.bin', 'wb') as file:
    for _ in range(num_records):
        id_num = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        gpa = float(input("Enter employee GPA: "))

        data = struct.pack('i20sif', id_num, name.encode(), age, gpa)
        file.write(data)

print(f"{num_records} records have been written to records.bin.")
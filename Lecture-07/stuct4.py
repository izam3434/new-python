import struct

record_format = "i20sif"
record_size = struct.calcsize(record_format)

with open("records.bin", "rb") as file:
    file.seek(record_size)
    data = file.read(record_size)

    record = struct.unpack(record_format, data)

    record_id = (record[0], record[1].decode().strip('\x00'), record[2], record[3])

    print(f"ID: {record_id[0]}, Name: {record_id[1]}, Age: {record_id[2]}, GPA: {record_id[3]}")
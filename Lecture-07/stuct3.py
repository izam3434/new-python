import struct

with open('records.bin', 'rb') as file:
    data = file.read(struct.calcsize('i20sif'))

    record = struct.unpack('i20sif', data)

    record_id = (record[0],record[1].decode().strip('\x00'), record[2], record[3])

    print(f"ID: {record_id[0]}, Name: {record_id[1]}, Age: {record_id[2]}, GPA: {record_id[3]}")
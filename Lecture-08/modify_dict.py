student = {"name": "Alice", "age": 25, "grade": "A"}

student["age"] = 26
student["major"] = "computer science"
print(student)

del student["grade"]
print(student)

removed_value = student.pop("major")
print(removed_value)
print(student)
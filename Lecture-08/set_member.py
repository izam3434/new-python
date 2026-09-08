fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("grape")
print(fruits)

removed_fruit = fruits.pop()
print(removed_fruit)
print(fruits)

fruits.clear()
print(fruits)
# Dictionary Example
mydic = {'A': 'Akash', 1: 'One', 9: 9, 'Z': 99, 'B': 'B'}

print(mydic)
print(mydic['A'])
print(mydic[1])


# Change Dictionary Value
mydic = {
    "name": "Akash",
    "age": 25
}

mydic["age"] = 26

print(mydic)


# Print Keys
mydic = {
    "name": "Akash",
    "city": "Ahmedabad",
    "course": "Python"
}

print(mydic.keys())


# Print Values
print(mydic.values())


# Print Keys and Values
print(mydic.items())


# Loop through Dictionary
for key, value in mydic.items():
    print(key, value)


# Add New Item
mydic["mobile"] = "9876543210"

print(mydic)


# Remove Item
mydic.pop("city")

print(mydic)


# Remove Last Item
mydic.popitem()

print(mydic)


# Delete Item
del mydic["course"]

print(mydic)


# Clear Dictionary
mydic.clear()

print(mydic)


# Copy Dictionary
mydic = {
    "name": "Akash",
    "city": "Ahmedabad"
}

newdic = mydic.copy()

print(newdic)


# Dictionary Length
print(len(mydic))


# Check Key Exists
if "name" in mydic:
    print("Key Found")
else:
    print("Key Not Found")


# User Input Dictionary
mydic = {}

n = int(input("Enter Number of Records: "))

for i in range(n):
    key = input("Enter Key: ")
    value = input("Enter Value: ")
    mydic[key] = value

print(mydic)

# Create Empty Set
empty_set = set()

print(empty_set)


# Create Set
myset = {10, 20, 30, 40, 50}

print(myset)


# Set Does Not Allow Duplicate Values
myset = {10, 20, 30, 20, 40, 50, 10}

print(myset)


# Create Set using set() Function
a = {"one": 1, "two": 2}
b = [100, 200, 300]
c = "python"

print(set(a))
print(set(b))
print(set(c))


# Add Single Item
myset = {1, 2}

myset.add(3)

print(myset)


# Add Multiple Items
myset = {1, 2}

myset.update([3, 4, 5])

print(myset)


# Remove Item using remove()
myset = {1, 2, 3, 4, 5}

myset.remove(3)

print(myset)


# Remove Item using discard()
myset = {1, 2, 3, 4, 5}

myset.discard(4)

print(myset)


# Clear Set
myset = {1, 2, 3, 4, 5}

myset.clear()

print(myset)


# Loop through Set
myset = {"Python", "Java", "PHP", "C"}

for i in myset:
    print(i)


# Check Item Exists
myset = {"Python", "Java", "PHP"}

if "Python" in myset:
    print("Item Found")
else:
    print("Item Not Found")


# Length of Set
myset = {10, 20, 30, 40, 50}

print(len(myset))


# Copy Set
set1 = {10, 20, 30}

set2 = set1.copy()

print(set2)


# Union
set1 = {"Maruti", "Hyundai", "Ford"}
set2 = {"Audi", "BMW", "Ford"}

print(set1 | set2)
print(set1.union(set2))


# Intersection
set1 = {"Na", "K", "Cl"}
set2 = {"HCL", "Cl", "Ba"}

print(set1 & set2)
print(set1.intersection(set2))


# Difference
set1 = {"Python", "JavaScript", "C++"}
set2 = {"Assembly", "C++"}

print(set1 - set2)
print(set1.difference(set2))

print(set2 - set1)
print(set2.difference(set1))


# Symmetric Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# Union
set1 = {"Maruti", "Hyundai", "Ford"}
set2 = {"Audi", "BMW", "Ford"}

print(set1 | set2)
print(set1.union(set2))


# Intersection
set1 = {"Na", "K", "Cl"}
set2 = {"HCL", "Cl", "Ba"}

print(set1 & set2)
print(set1.intersection(set2))


# Difference
set1 = {"Python", "JavaScript", "C++"}
set2 = {"Assembly", "C++"}

print(set1 - set2)
print(set1.difference(set2))


# Symmetric Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 ^ set2)
print(set1.symmetric_difference(set2))
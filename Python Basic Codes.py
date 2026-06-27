print("Hello World")
a = 10
print(a)
a = "Jhanvi"
print(a)

a = input(int("enter a num 1:"))
b = input(int("enter a num 2:"))
c = a + b

# Method 1
print("A is ",a)
print("")

"""
Multiline 
comment
"""
#Single line comment

a = int(input("Enter No1: "))
b = int(input("Enter No2: "))

c = a + b

# Method 1
print("A is ", a)
print("B is ", b)
print("C is ", c)

# Method 2
print("\nA is ", a, "\nB is ", b, "\nSum is ", c)

# Method 3
print("A is {}\nB is {}\nSum is {}".format(a, b, c))

# Method 4 (f-string)
print(f"A is {a}\nB is {b}\nSum is {c}")

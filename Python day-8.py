mylist1 = [10, 20, 30, 40, 50]
mylist2 = [10, "C", 99, 25.50, "PHP"]

print(mylist1)
print(mylist2)

mylist1 = [10, "C", 99, 25.50, "PHP", 88, 45, 99]

print(mylist1)          
print(mylist1[2])      
print(mylist1[4:6])     
print(mylist1[3:])  

mylist = [10, 20, 30, 40]

mylist[1] = 100

print(mylist)

mylist = [10, 20, 30, 40, 50]

print(len(mylist))

list1 = [10, 20, 30]
list2 = [40, 50, 60]

print(list1 + list2)

list1 = [10, 20]

print(list1 * 3)

mylist = [10, 20, 30, 40, 50]

for i in mylist:
    print(i)

    mylist = []

no = int(input("Enter Number of Element: "))

for i in range(no):
    value = input("Enter Value: ")
    mylist.append(value)

print(mylist)

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(matrix)

print(matrix[0])
print(matrix[1][2])

mylist = [10, 20, 30]

mylist.append(40)

print(mylist)

mylist = [10, 20, 40]

mylist.insert(2, 30)

print(mylist)

mylist = [10, 20, 30, 40]

mylist.remove(30)

print(mylist)

mylist = [10, 20, 30, 40]

mylist.pop()

print(mylist)

mylist = [50, 10, 40, 20, 30]

mylist.sort()

print(mylist)

mylist = [10, 20, 30, 40]

mylist.reverse()

print(mylist)

mylist = [10, 20, 30]

mylist.clear()

print(mylist)

list1 = [10, 20, 30]

list2 = list1.copy()

print(list2)

# TUPLE 

mytuple = (10, "C", 99, 25.50, "PHP", 88, 45, 99)

print(mytuple)

mytuple = (10, "C", 99, 25.50, "PHP", 88, 45, 99)

print(mytuple)       
print(mytuple[2])     
print(mytuple[4:6])   
print(mytuple[3:]) 

mytuple = ("Python", "Java", "PHP", "C")

print(mytuple[0])
print(mytuple[2])

mytuple = (10, 20, 30, 40, 50)

print(len(mytuple))

mytuple = (10, 20, 30, 40, 50)

for i in mytuple:
    print(i)

mylist = []

no = int(input("Enter Number of Elements: "))

for i in range(no):
    value = input("Enter Value: ")
    mylist.append(value)

mytuple = tuple(mylist)

print(mytuple)

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

print(tuple1 + tuple2)

tuple1 = (10, 20)

print(tuple1 * 3)

mytuple = (10, 20, 30, 40)

print(20 in mytuple)
print(100 in mytuple)

mytuple = (10, 20, 30, 20, 40)

print(mytuple.count(20))

mytuple = (10, 20, 30, 40)

print(mytuple.index(30))

mytuple = (
    (10, 20),
    (30, 40),
    (50, 60)
)

print(mytuple)
print(mytuple[1])
print(mytuple[2][0])

mylist = [10, 20, 30, 40]

mytuple = tuple(mylist)

print(mytuple)

mytuple = (10, 20, 30, 40)

mylist = list(mytuple)

print(mylist)

mytuple = (10, 20, 30)

# Error
# mytuple[1] = 100

print(mytuple)
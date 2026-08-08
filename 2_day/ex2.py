import math

first_name = "cristiano"
last_name = "ronaldo"

x1 = 2
x2 = 1

total = x1 + x2
diff = x1 - x2
prod = x1 * x2
mod = x1 % x2
exp = x1 ** x2
floor = x1 // x2

print("Last name length: " + str(len(last_name)))
print(len(last_name) > len(first_name))
print(total)


radius = float(input("Declare the radius of circle: "))

circum = (math.pi * 2) * radius
area = math.pi * radius ** 2

print(circum)
print(area)
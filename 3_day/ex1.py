import math

age = int(input("What is your age: "))
height = float(input("What is your height: "))

real = float(input("Declare the real part: "))
imaginary = float(input("Declare the imaginary part: "))

comp = complex(real, imaginary)

base = float(input("Declare the base: "))
height = float(input("Declare the height: "))
print(base * 0.5 * height)

side_a = float(input("Declare side a: "))
side_b = float(input("Declare side b: "))
side_c = float(input("Declare side c: "))
print(side_a + side_b + side_c)

length = float(input("Declare the length of the rectagle: "))
width = float(input("Declare the width of the rectangle: "))
print(2 *(length + width))

radius = float(input("Declare the radius: "))
print("Area: ", math.pi * radius ** 2)
print("Circumference: ", math.pi * radius * 2)

x1 = int(input("Declare x1: "))
x2 = int(input("Declare x2: "))
y1 = int(input("Declare y1: "))
y2 = int(input("Declare y2: "))
slope = (y2 - y1) / (x2-x1)
print("Slope: ", slope)
print("Euclidian distance: ", math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

print("S1 > S2?: ", 2 > slope)


x = int(input("Declare the value of x: "))
print("y = ", x**2 + 6 * x + 9)

print("y = 0 when x1 = ", (-6 + math.sqrt(6**2 - 4*9)) / 2, "x2 = ", (-6 - math.sqrt(6**2 - 4*9)) / 2  )

print("Length of python: ", len("python"))
print("Length of dragon: ", len("dragon"))
print("L_dragon > L_python: ", len("dragon") > len("python"))

if ('on' in 'python' and 'on' in 'dragon'):
    print("On is found in both python and dragon")
elif ('on' not in 'python' and 'on' not in 'dragon'):
    print("on is not found in both python and dragon")
else:
    print("on is not present in one of them")


if ('jargon' in 'Ihope this course is not full of jargon'):
    print("True")
else:
    print("False")


print(str(float(len('python'))))


x = int(input("Declare a number: "))
if (x % 2 == 1):
    print("The declared number is odd")
else:
    print("The declared number is even:")


if(7//3 == int(2.7)):
    print("The values are equal")
else:
    print("The values are not equal")


if(type(10) == type('10')):
    print("The types are the same")
else:
    print("The types are not the same")


if(10 == int(float(('9.8')))):
    print("The values are equal")
else:
    print("The values are not equal")


ore = int(input("Declare the number of hours "))
per_hour = int(input("Declare the hourly rate: "))
print("The weekly earning is: ", ore * per_hour * 5)


year = int(input("Enter the number of years that you have lived: "))
if (year <= 100):
    print("You have lived ", year * 365 * 24 * 60 * 60, "seconds")


for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
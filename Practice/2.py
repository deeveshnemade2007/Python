class Student:
    college_name = "NMIET"
    def __init__(self, roll_no, name, percent):  
        self.roll_no = roll_no
        self.name = name
        self.percent = percent  
        self.email = self.name + "@" + Student.college_name + ".com"
    def display_detail(self):
        print("College Name:", Student.college_name)
        print("Roll No.:", self.roll_no)
        print("Name:", self.name)
        print("Percent:", self.percent)
        print("Email:", self.email)
roll_no = int(input("Enter Roll No.: "))
name = input("Enter Name: ")
percent = float(input("Enter Percentage: "))
s1 = Student(roll_no, name, percent)
s1.display_detail()




class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
base = float(input("Enter base: "))
height = float(input("Enter height: "))
t = Triangle(base, height)
print("Area of Triangle = ", t.area())


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
length = float(input("\nEnter length: "))
breadth = float(input("Enter breadth: "))
r = Rectangle(length, breadth)
print("Area of Rectangle =", r.area())


class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
side = float(input("\nEnter side: "))
s = Square(side)
print("Area of Square =", s.area())\


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
radius = float(input("\nEnter radius: "))
c = Circle(radius)
print("Area of Circle =", c.area())
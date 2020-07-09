import math
import matplotlib.pyplot as plt

class triangle: 
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.area = 0
        self.inscribed_radius = 0
        self.circumscribed_radius = 0
        self.x_coordinates = []
        self.y_coordinates = []
    def state(self):
        print("Here are the properties of the triangle:")
        print("a = {}".format(self.a))
        print("b = {}".format(self.b))
        print("c = {}".format(self.c))
        print("A = {}".format(self.A))
        print("B = {}".format(self.B))
        print("C = {}".format(self.C))
        if self.equilateral_check(): 
            print("This is an equilateral triangle")
        if self.isosceles_check():
            print("This is a isosceles triangle")
        if self.right_check():
            print("This is a right triangle")
        print("Area = {}".format(self.area))
        print("Radius of inscribed cirle is {}".format(self.inscribed_radius))
        print("Radius of circumscribed circle is {}".format(self.circumscribed_radius))
    def measure_angle(self): 
        self.A = round(math.degrees(math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c))), 2)
        self.B = round(math.degrees(math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))), 2)
        self.C = round(math.degrees(math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b))), 2)
    def measure_area(self):
        area1 = 0.5 * self.a * self.b * math.sin(math.radians(self.C))
        area2 = 0.5 * self.b * self.c * math.sin(math.radians(self.A))
        area3 = 0.5 * self.a * self.c * math.sin(math.radians(self.B))
        self.area = round((area1 + area2 + area3) / 3, 2)
    def coordinate(self):
        A_x = 0
        A_y = 0
        B_x = math.cos(math.radians(self.A)) * self.c
        B_y = math.sin(math.radians(self.A)) * self.c
        C_x = self.b
        C_y = 0
        self.x_coordinates = [A_x, B_x, C_x, A_x]
        self.y_coordinates = [A_y, B_y, C_y, A_y]
    def measure_inscribed_radius(self):
        self.inscribed_radius = round(2 * self.area / (self.a + self.b + self.c), 2)
    def measure_circumscribed_radius(self):
        circumscribed_radius1 = self.a / (2 * math.sin(math.radians(self.A)))
        circumscribed_radius2 = self.b / (2 * math.sin(math.radians(self.B)))
        circumscribed_radius3 = self.c / (2 * math.sin(math.radians(self.C)))
        self.circumscribed_radius = round((circumscribed_radius1 + circumscribed_radius2 + circumscribed_radius3) / 3, 2)
    def integrity_check(self):
        if (self.a + self.b <= self.c): 
            return False
        if (self.b + self.c <= self.a):
            return False
        if (self.a + self.c <= self.b):
            return False
        return True
    def right_check(self):
        if (self.A == 90) or (self.B == 90) or (self.C) == 90: 
            return True
        return False
    def equilateral_check(self): 
        if (self.a == self.b) and (self.b == self.c): 
            return True
        return False
    def isosceles_check(self):
        if not self.equilateral_check():
            if (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
                return True
        return False
    def process_triangle(self):
        self.measure_angle()
        self.measure_area()
        self.measure_inscribed_radius()
        self.measure_circumscribed_radius()
        self.coordinate()
        self.state()

if __name__ == '__main__':
    Triangle = triangle()
    print('Please input the side length for your triangle.')
    while True: 
        Triangle.a = float(input("Input a: "))
        Triangle.b = float(input("Input b: "))
        Triangle.c = float(input("Input c: "))
        if not Triangle.integrity_check(): 
            print("It is an invalid Triangle!")
        else: 
            Triangle.process_triangle()
            plt.plot(Triangle.x_coordinates, Triangle.y_coordinates, color = 'green', linewidth = 3)
            plt.show()

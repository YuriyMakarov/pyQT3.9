'''Задача про треугольники'''
import math
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.existence()
        self.type_triangle()
        self.angle_type()
        self.perimeter()
        self.square()

    def existence(self):
        '''Проверка на возможность создания треугольника'''
        if (self.side1 >= self.side2 + self.side3 or self.side2 >= self.side1 + self.side3 or
        self.side3 >= self.side1 + self.side2):
            self.existence = "не существует"
        else:
            self.existence = "существует"

    def type_triangle(self):
        '''Определение вида треугольника по сторонам'''
        if (self.side1 == self.side2 == self.side3):
            self.type_triangle = "равносторонний"

        elif (self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3):
            self.type_triangle = "равнобедренный"

        elif (self.side1 != self.side2 != self.side3):
            self.type_triangle = "разносторонний"

    def angle_type(self):
        '''Определение вида треугольника по углу'''
        sides = [self.side1, self.side2, self.side3]
        hypotenuse = max(sides)
        sides.remove(max(sides))
        legs = []
        for side in sides:
            side = pow(side, 2)
            legs.append(side)

        if pow(hypotenuse, 2) > (sum(legs)):
            self.angle_type = "тупоугольный"
        elif pow(hypotenuse, 2) == (sum(legs)):
            self.angle_type = "прямоугольный"
        elif pow(hypotenuse, 2) < (sum(legs)):
            self.angle_type = "остроугольный"

    def perimeter(self):
        '''Нахождение периметра'''
        self.perimeter = self.side1 + self.side2 + self.side3



    def square(self):
        '''Нахождение площади треугольника по формуле Герона'''
        p = (self.side1 + self.side2 + self.side3)/2
        if (p*(p-self.side1)*(p-self.side2)*(p-self.side3)) > 0:
            self.square = math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
            self.square = format(self.square,'.2f')

    def print_info(self):
        '''Вывод информации о треугольнике, если он существует'''
        if self.existence == "не существует":
            print("Треугольник не существует")
        else:
            print(f"Ваш треугольник {self.existence}, он {self.type_triangle} и {self.angle_type}, "
              f"имеет периметр {self.perimeter} и площадь {self.square}")


my_triangle = Triangle(1,2,5)
my_triangle.print_info()



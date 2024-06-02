#Task 2
class Triangle:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.h = None

    def set_sideA(self, sideA):
        if sideA > 0:
            self.a = sideA

    def set_sideB(self, sideB):
        if sideB > 0:
            self.b = sideB

    def set_sideC(self, sideC):
        if sideC > 0:
            self.c = sideC

    def set_height(self, height):
        if height > 0:
            self.h = height

    def get_sideA(self):
        return self.a

    def get_sideB(self):
        return self.b

    def get_sideC(self):
        return self.c

    def get_height(self):
        return self.h

    def get_per(self):
        if (self.a is None) + (self.b is None) + (self.c is None) == 0:
            return self.a + self.b + self.c
        elif (self.a is None) + (self.b is None) + (self.c is None) == 1:
            if self.a is None:
                return self.b + self.c + self.get_square()
            elif self.b is None:
                return self.a + self.c + self.get_square()
            elif self.c is None:
                return self.b + self.a + self.get_square()
        else:
            return "Ошибка"

    def calc_square_gerron(self):
        p = self.get_per() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def calc_square_height(self):
        print(0.5 * self.a * self.h, "hhh")
        return 0.5 * self.a * self.h

    def get_square(self):
        if 1 <= (self.a is None or self.b is None or self.c is None) <= 2 and self.h is not None:
            return self.calc_square_height()
        elif (self.a is None) + (self.b is None) + (self.c is None) == 0:
            return self.calc_square_gerron()
        else:
            return "Ошибка"


t = Triangle()
t.set_height(4)
t.set_sideA(3)
t.set_sideB(4)
t.set_sideC(5)
res_sq = t.get_square()
res_per = t.get_per()
print(f'{res_sq}, \n{res_per}')

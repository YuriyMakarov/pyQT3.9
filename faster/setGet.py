class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        if 0 < age <= 100:
            print("Бодрячом")
        else:
            print("Не бодрячком")


mark = Person("Марк", 101)
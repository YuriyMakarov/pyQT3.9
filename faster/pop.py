# Словари
# my_dict = {
#     'name': 'Nikta',
#     'age': 24,
#     'surname': 'Belikov'
# }
#
# my_dict['вес'] = 70
# my_dict['name'] = 'Maksim'
# del my_dict['age']
# print(my_dict)
#
# for key, value in my_dict.items():
#     print(f'{key} >>> {value}')

# Словари
# ДЗ
# Задание 1
# names = {
#     input('Напиши ключ: '):input('Напиши имя: '),
#     input('Напиши ключ: '):input('Напиши имя: '),
#     input('Напиши ключ: '):input('Напиши имя: '),
#     input('Напиши ключ: '):input('Напиши имя: '),
# }
#
# print(names)

# Задание 2
# def students_grade(students_dict, target_grade):
#     result_students = []
#
#     for student, grade in students_dict.items():
#         if grade == target_grade:
#             result_students.append(student)
#
#     return result_students
#
#
# # Пример использования:
# students_grades = {
#     "Иванов": 4,
#     "Петров": 5,
#     "Сидоров": 3,
#     "Андреев": 4,
#     "Козлов": 5
# }
#
# target_grade = 3
# result_students = students_grade(students_grades, target_grade)
#
# print(f"Студенты с оценкой {target_grade}: {result_students}")

# Классы
# Задание 1
# class Train:
#     def __init__(self, destination_name, train_number, departure_time):
#         self.destination_name = destination_name
#         self.train_number = train_number
#         self.departure_time = departure_time
#
#     def __str__(self):
#         return f"Train Number: {self.train_number}, Destination: {self.destination_name}, Departure Time: {self.departure_time}"
#
#
# def display_train_info(trains, train_number):
#     for train in trains:
#         if train.train_number == train_number:
#             print(train)
#             break
#     else:
#         print("Train not found.")
#
#
# trains = [
#     Train("New York", 123, "10:00"),
#     Train("Los Angeles", 456, "14:00"),
#     Train("Chicago", 789, "18:00"),
#     Train("Boston", 101, "22:00"),
#     Train("Houston", 111, "02:00")
# ]
#
# train_number_to_search = int(input("Enter train number to search: "))
# display_train_info(trains, train_number_to_search)

# Задание 2
# class MyClass:
#    def __init__(self, var1, var2):
#        self.var1 = var1
#        self.var2 = var2
#
#    def display_variables(self):
#        print(f"var1: {self.var1}, var2: {self.var2}")
#
#    def change_variables(self, new_var1, new_var2):
#        self.var1 = new_var1
#        self.var2 = new_var2
#
#    def find_sum(self):
#        return self.var1 + self.var2
#
#    def find_largest(self):
#        return max(self.var1, self.var2)
#
#
# my_obj = MyClass(5, 10)
# my_obj.display_variables()
# print("Sum of the variables:", my_obj.find_sum())
# print("Largest value between the variables:", my_obj.find_largest())
# my_obj.change_variables(15, 20)
# my_obj.display_variables()
# print("Sum of the variables:", my_obj.find_sum())
# print("Largest value between the variables:", my_obj.find_largest())

# Задача 3
# class Children:
#    def __init__(self, first_name, last_name, age):
#        self.first_name = first_name
#        self.last_name = last_name
#        self.age = age
#
#    def enter_data(self):
#        self.first_name = input("Enter child's first name: ")
#        self.last_name = input("Enter child's last name: ")
#        self.age = int(input("Enter child's age: "))
#
#    def display_data(self):
#        print(f"Child's name: {self.first_name} {self.last_name}")
#        print(f"Child's age: {self.age}")
#
#
# child1 = Children("", "", 0)
# child2 = Children("", "", 0)
#
# child1.enter_data()
# child1.display_data()
#
# child2.enter_data()
# child2.display_data()

# Наследование
# Задача 1
# class Person:
#    def __init__(self, first_name, last_name, number_of_lessons):
#        self.first_name = first_name
#        self.last_name = last_name
#        self.number_of_lessons = number_of_lessons
#
#
# class Student(Person):
#    def __init__(self, first_name, last_name, number_of_lessons, grades):
#        super().__init__(first_name, last_name, number_of_lessons)
#        self.grades = grades
#
#
# class Teacher(Person):
#    def __init__(self, first_name, last_name, number_of_lessons, salary):
#        super().__init__(first_name, last_name, number_of_lessons)
#        self.salary = salary
#
#
# student1 = Student("John", "Doe", 10, [85, 90, 88])
# teacher1 = Teacher("Jane", "Doe", 15, 50000)
#
# print("Student data:")
# print(f"First name: {student1.first_name}")
# print(f"Last name: {student1.last_name}")
# print(f"Number of lessons: {student1.number_of_lessons}")
# print(f"Grades: {student1.grades}")
#
# print("Teacher data:")
# print(f"First name: {teacher1.first_name}")
# print(f"Last name: {teacher1.last_name}")
# print(f"Number of lessons: {teacher1.number_of_lessons}")
# print(f"Salary: {teacher1.salary}")

# Задача 2
# class Cat:
#    def __init__(self, breed, age, nickname, sex):
#        self._breed = breed
#        self._age = age
#        self._nickname = nickname
#        self._sex = sex
#
#    @property
#    def breed(self):
#        return self._breed
#
#    @breed.setter
#    def breed(self, breed):
#        self._breed = breed
#
#    @property
#    def age(self):
#        return self._age
#
#    @age.setter
#    def age(self, age):
#        if 0 <= age <= 20:
#            self._age = age
#        else:
#            print("Inappropriate age")
#
#    @property
#    def nickname(self):
#        return self._nickname
#
#    @nickname.setter
#    def nickname(self, nickname):
#        self._nickname = nickname
#
#    @property
#    def sex(self):
#        return self._sex
#
#    @sex.setter
#    def sex(self, sex):
#        if sex == "M" or sex == "W":
#            self._sex = sex
#        else:
#            print("Unknown gender")
#
#
# cat1 = Cat("Persian", 5, "Whiskers", "M")
# cat1.age = 15
# cat1.nickname = "Whiskers2"
# cat1.sex = "F"
#
# print("Cat data:")
# print(f"Breed: {cat1.breed}")
# print(f"Age: {cat1.age}")
# print(f"Nickname: {cat1.nickname}")
# print(f"Sex: {cat1.sex}")

# Задача 3
# class Animal:
#    def __init__(self, species, age, nickname):
#        self.species = species
#        self.age = age
#        self.nickname = nickname
#
#    def display_info(self):
#        print(f"Species: {self.species}, Age: {self.age}, Nickname: {self.nickname}")
#
#
# class Kennel:
#    def __init__(self, kennel_name):
#        self.kennel_name = kennel_name
#        self.animals = []
#
#    def add_animal(self, animal):
#        self.animals.append(animal)
#
#    def delete_animal(self, nickname):
#        for animal in self.animals:
#            if animal.nickname == nickname:
#                self.animals.remove(animal)
#                return
#        print("Animal not found")
#
#    def find_animal_by_species(self, species):
#        for animal in self.animals:
#            if animal.species == species:
#                animal.display_info()
#                return
#        print("Animal not found")
#
#
# kennel1 = Kennel("Kennel1")
# animal1 = Animal("Dog", 5, "Buddy")
# animal2 = Animal("Cat", 3, "Whiskers")
#
# kennel1.add_animal(animal1)
# kennel1.add_animal(animal2)
#
# kennel1.find_animal_by_species("Dog")
# kennel1.delete_animal("Whiskers")
# kennel1.find_animal_by_species("Cat")

# Задача 4

class Abiturient:
    def __init__(self, name):
        self.name = name
        self.score_exams = {}

    def registrate(self, faculty):
        faculty.abiturients.append(self)

    def take_exam(self, faculty, exam, score):
        find_exam = None
        for examen in faculty.exams:
            if examen.name == exam:
                find_exam = examen
                break

        if find_exam is None:
            print("Такого экзамента нет на данном факультете")
        elif find_exam.min_mark <= score:
            self.score_exams[find_exam.name] = score
        else:
            self.score_exams[find_exam.name] = "Не сдал"


class Faculty:
    def __init__(self, name, min_score):
        self.name = name
        self.students = []
        self.abiturients = []
        self.exams = []
        self.min_score = min_score

    def zachisl(self, abiturient):
        if "Не сдал" not in abiturient.score_exams.values():
            total_score = sum(abiturient.score_exams.values())
            print(total_score)
            if total_score >= self.min_score:
                print("Студент зачислен")
                self.students.append(abiturient)
                self.abiturients.remove(abiturient)
            else:
                print("Студент не зачислен")
        else:
            print("Студент не зачислен")


class Exam:
    def __init__(self, name, min_mark):
        self.name = name
        self.min_mark = min_mark





mark = Abiturient("Марк")
fct = Faculty("ФКТиПМ", 244)
ex1 = Exam("Математика", 48)
ex2 = Exam("Русский", 42)
ex3 = Exam("Информатика", 47)
fct.exams.append(ex1)
fct.exams.append(ex2)
fct.exams.append(ex3)

mark.registrate(fct)
mark.take_exam(fct, "Математика", 100)
mark.take_exam(fct, "Русский", 100)
mark.take_exam(fct, "Информатика", 99)

fct.zachisl(mark)

for student in fct.students:
    print(student.name)


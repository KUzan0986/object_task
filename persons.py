def mid_rate(person):
    if isinstance(person, Lecturer) or isinstance(person, Student):
        summa = 0
        num = 0
        for i in person.grades:
            summa += sum(person.grades[i])
            num += len(person.grades[i])
        try:
            return summa/num
        except ZeroDivisionError:
            return 0


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lector, course, rate):
        if not isinstance(lector, Lecturer):
            print("Это не лектор!")
        else:
            if course in lector.courses_attached:
                try:
                    lector.grades[course].append(rate)
                except BaseException:
                    lector.grades[course] = [rate]
            else:
                print(f"{lector.name} {lector.surname} не ведет курс {course}")

    def dcourses_in_progress(self):
        res = ""
        for i in self.courses_in_progress:
            res += i + ", "
        res = res[0:len(res) - 2]
        return res

    def dfinished_courses(self):
        res = ""
        for i in self.finished_courses:
            res += i + ", "
        res = res[0:len(res)-2]
        return res

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {mid_rate(self)}\n\
Курсы в процессе изучения: {self.dcourses_in_progress()}\nЗавершенные курсы: {self.dfinished_courses()}"

    def __lt__(self, studento):
        return mid_rate(self) < mid_rate(studento)

    def __le__(self, studento):
        return mid_rate(self) <= mid_rate(studento)



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {mid_rate(self)}"

    def __lt__(self, reviewer):
        return mid_rate(self) < mid_rate(reviewer)

    def __le__(self, reviewer):
        return mid_rate(self) <= mid_rate(reviewer)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"



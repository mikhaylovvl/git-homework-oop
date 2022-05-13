from collections import defaultdict
from statistics import mean

from Tools.scripts.mkreal import join


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lector, course, grade):
        if 1 <= grade <= 10:
            if isinstance(lector,
                          Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
                lector.courses_grade[course].append(grade)
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def count_avg(self):
        sum_grade = 0
        count_grade = 0
        for value in self.grades.values():
            sum_grade += sum(value)
            count_grade += len(value)
        if count_grade == 0:
            print('Нет оценок')
            return
        else:
            return sum_grade / count_grade

    def __lt__(self, other):
        return self.count_avg() < other.count_avg()

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.count_avg()}' \
              f' \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_grade = defaultdict(list)

    def count_avg(self):
        sum_rate = 0
        count_rate = 0
        for value in self.courses_grade.values():
            sum_rate += sum(value)
            count_rate += len(value)
        if count_rate == 0:
            print('Нет оценок')
            return
        else:
            return sum_rate / count_rate

    def __lt__(self, other):
        return self.count_avg() < other.count_avg()

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.count_avg()}'
        return res


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
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


vladimir_rev = Reviewer('Vladimir', 'Mikhaylov')
vladimir_rev.courses_attached = ['Python', 'C#', 'Web-Designe']

jon_student = Student('Jon', 'Persiv', 'Man')
jon_student.courses_in_progress = ['Python', 'C#']
jon_student.finished_courses = ['Введение в программирование', 'Web-Designe']

milana_student = Student('Milana', 'Dub', 'Womam')
milana_student.courses_in_progress = ['Введение в программирование', 'Web-Designe', 'C#']

vladimir_rev.rate_hw(jon_student, 'Python', 7)
vladimir_rev.rate_hw(jon_student, 'C#', 10)
vladimir_rev.rate_hw(jon_student, 'C#', 8)

alex_lecturer = Lecturer('Alex', 'Gahan')
alex_lecturer.courses_attached = ['C#', 'Java from zero', 'Web-Designe']
ben_lecturer = Lecturer('Ben', 'Aflic')
ben_lecturer.courses_attached = ['Введение в программирование', 'Web-Designe']
milana_student.rate_lecture(ben_lecturer, 'Введение в программирование', 7)
milana_student.rate_lecture(ben_lecturer, 'Web-Designe', 10)
milana_student.rate_lecture(alex_lecturer, 'Web-Designe', 8)
milana_student.rate_lecture(alex_lecturer, 'Web-Designe', 9)

victor_student = Student('Victor', 'Padalka', 'Man')
victor_student.courses_in_progress = ['Java from zero', 'C#']
victor_student.rate_lecture(alex_lecturer, 'Java from zero', 9)
victor_student.rate_lecture(alex_lecturer, 'Java from zero', 10)
victor_student.rate_lecture(alex_lecturer, 'C#', 8)

vladimir_rev.rate_hw(milana_student, 'C#', 9)
vladimir_rev.rate_hw(milana_student, 'Web-Designe', 10)

print(jon_student.grades)
print()
print(dict(ben_lecturer.courses_grade))
print()
print(dict(alex_lecturer.courses_grade))
print()
print(vladimir_rev)
print()
print(alex_lecturer)
print()
print(jon_student)
print()
print(alex_lecturer.count_avg() < ben_lecturer.count_avg())
print()
print(milana_student.count_avg() > jon_student.count_avg())
print()

stesha = Student('Stesha', 'Mikhaylova', 'Woman')
stesha.courses_in_progress = ['C#']
stesha.finished_courses = ['Java from zero']
svetlana = Student('Svetlana', 'Kojohar', 'Woman')
stesha.rate_lecture(alex_lecturer, 'C#', 8)
stesha.count_avg()
svetlana.rate_lecture(ben_lecturer, 'Web-Designe', 10)
svetlana.count_avg()

igor = Lecturer('Igor', 'Ivanov')
ruslan = Lecturer('Ruslan', 'Trifon')
igor.count_avg()
ruslan.count_avg()

ivan = Reviewer('Ivan', 'Berezin')
ivan.courses_attached = ['C#']
evgeniy = Reviewer('Evgeniy', 'Podubny')
ivan.rate_hw(stesha, 'C#', 10)
evgeniy.rate_hw(svetlana, 'Java from zero', 9)
vladimir_rev.rate_hw(milana_student, 'C#', 9)
vladimir_rev.rate_hw(milana_student, 'C#', 10)


def count_avg_grade_students_course(list_students, course):
    sum_grade = 0
    len_grade = 0
    for idx in list_students:
        for key, value in idx.grades.items():
            if key == course:
                sum_grade += sum(value)
                len_grade += len(value)
    return sum_grade / len_grade


def count_avg_grade_lectures(list_lectures, course):
    sum_grade = 0
    len_grade = 0
    for idx in list_lectures:
        for key, value in idx.courses_grade.items():
            if key == course:
                sum_grade += sum(value)
                len_grade += len(value)
    return sum_grade / len_grade


list_students = [jon_student, milana_student, stesha]
course_s = 'C#'

print(count_avg_grade_students_course(list_students, course_s))

list_lectures = [alex_lecturer, ben_lecturer]
course_l = 'Web-Designe'

print(count_avg_grade_lectures(list_lectures, course_l))

print(ben_lecturer.__lt__(alex_lecturer))
print(alex_lecturer.__lt__(ben_lecturer))

print(milana_student.__lt__(jon_student))
print(jon_student.__lt__(milana_student))
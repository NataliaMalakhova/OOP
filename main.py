class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}

  def rate_lecture(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
          if course in lecturer.grades:
              lecturer.grades[course].append(grade)
          else:
              lecturer.grades[course] = [grade]
      else:
          return 'Ошибка'

  def __str__(self):
      total_grades = []
      for grades in self.grades.values():
          total_grades.extend(grades)
      average_grade = sum(total_grades) / len(total_grades) if total_grades else 0
      courses_in_progress_str = ', '.join(self.courses_in_progress)
      finished_courses_str = ', '.join(self.finished_courses)
      return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}'

  def __lt__(self, other):
      if isinstance(other, Student):
          return self._average_grades() < other._average_grades()
      return NotImplemented

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
      total_grades = []
      for grades in self.grades.values():
          total_grades.extend(grades)
      average_grade = sum(total_grades) / len(total_grades) if total_grades else 0
      return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}'

  def __lt__(self, other):
      if isinstance(other, Lecturer):
          return self._average_grades() < other._average_grades()
      return NotImplemented

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
      return f'Имя: {self.name}\nФамилия: {self.surname}'

# Создание экземпляров классов и демонстрация работы методов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

class Mentor:

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):

    def __str__(self):
        average_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]
                            ) / len(self.grades) if self.grades else 'Нет оценок'
        return super().__str__() + f'\nСредняя оценка за лекции: {average_grade}'


class Reviewer(Mentor):

    def __str__(self):
        return super().__str__()


class Student:

    def __str__(self):
        average_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]
                            ) / len(self.grades) if self.grades else 'Нет оценок'
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {average_grade}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

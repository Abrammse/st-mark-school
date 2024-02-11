
from django.db import models
class Subject(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Selector(models.Model):
    GRADE_CHOICES = (
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D', 'D'),
        ('F', 'F'),
    )

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default='A+')

    def __str__(self):
        return f"{self.subject} - {self.grade}"


class Student(models.Model):
    idschool = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    cla = models.CharField(max_length=100)
    التقديرالعام = models.CharField(max_length=100,)
    password = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Selector)

    def __str__(self):
        return self.username

    def total_grade(self):
        grade_values = {
            'A': 4.0,
            'A-': 3.7,
            'B+': 3.3,
            'B': 3.0,
            'B-': 2.7,
            'C+': 2.3,
            'C': 2.0,
            'C-': 1.7,
            'D': 1.0,
            'F': 0.0,
        }

        total_credits = len(self.subjects.all()) * 3
        total_weighted_grade = sum([grade_values.get(selector.grade, 0) * 3 for selector in self.subjects.all()])

        if total_credits != 0:
            gpa = total_weighted_grade / total_credits
            return gpa
        else:
            return 0.0




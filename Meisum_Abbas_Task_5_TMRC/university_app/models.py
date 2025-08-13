from django.db import models
from django.db.models import Count, QuerySet

class CourseQuerySet(QuerySet):
    def with_student_count(self):
        return self.annotate(student_count=Count('students'))

class StudentQuerySet(QuerySet):
    def in_department(self, dept_id: int):
        return self.filter(course__department_id=dept_id)

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')

    # attach custom queryset
    objects = CourseQuerySet.as_manager()

    def __str__(self):
        return f"{self.name} ({self.department.name})"

class Student(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

    objects = StudentQuerySet.as_manager()

    def __str__(self):
        return self.name

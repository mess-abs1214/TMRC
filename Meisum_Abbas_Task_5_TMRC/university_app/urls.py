from django.urls import path
from .views import (
    DepartmentListCreate, DepartmentDetail,
    CourseListCreate, CourseDetail,
    StudentListCreate, StudentDetail,
    students_by_department, courses_with_counts
)

urlpatterns = [
    # Departments
    path('departments/', DepartmentListCreate.as_view()),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),
    path('departments/<int:dept_id>/students/', students_by_department),

    # Courses
    path('courses/', CourseListCreate.as_view()),
    path('courses/<int:pk>/', CourseDetail.as_view()),
    path('courses-with-counts/', courses_with_counts),

    # Students
    path('students/', StudentListCreate.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view()),
]

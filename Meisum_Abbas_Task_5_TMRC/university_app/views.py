from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Department, Course, Student
from .serializers import DepartmentSerializer, CourseSerializer, StudentSerializer

# ---- Generic CRUD ----
class DepartmentListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.select_related('department').prefetch_related('students').all().order_by('id')
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.select_related('department').prefetch_related('students').all()
    serializer_class = CourseSerializer

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.select_related('course', 'course__department').all().order_by('id')
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.select_related('course', 'course__department').all()
    serializer_class = StudentSerializer

# ---- Function-Based View (custom) ----
# Return all students of a given department (uses custom queryset)
@api_view(['GET'])
def students_by_department(request, dept_id: int):
    # 404 if department doesn't exist (cleaner API)
    get_object_or_404(Department, pk=dept_id)
    qs = Student.objects.in_department(dept_id).select_related('course', 'course__department')
    ser = StudentSerializer(qs, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)

# Another handy endpoint: courses with student counts (uses queryset method)
@api_view(['GET'])
def courses_with_counts(request):
    qs = Course.objects.with_student_count().select_related('department').order_by('-student_count', 'id')
    data = [
        {
            'id': c.id,
            'name': c.name,
            'department': {'id': c.department.id, 'name': c.department.name},
            'student_count': c.student_count
        }
        for c in qs
    ]
    return Response(data, status=status.HTTP_200_OK)

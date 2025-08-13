from rest_framework import serializers
from .models import Department, Course, Student

# tiny nested serializers for nice read output
class DepartmentMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')

class CourseMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name')

class CourseNestedSerializer(serializers.ModelSerializer):
    department = DepartmentMiniSerializer(read_only=True)
    class Meta:
        model = Course
        fields = ('id', 'name', 'department')

class StudentSerializer(serializers.ModelSerializer):
    # read: full course object
    course = CourseNestedSerializer(read_only=True)
    # write: pass just the id
    course_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Course.objects.all(), source='course'
    )

    class Meta:
        model = Student
        fields = ('id', 'name', 'course', 'course_id')

class CourseSerializer(serializers.ModelSerializer):
    department = DepartmentMiniSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Department.objects.all(), source='department'
    )
    # show enrolled students (read-only)
    students = serializers.SerializerMethodField(read_only=True)

    def get_students(self, obj):
        return [{'id': s.id, 'name': s.name} for s in obj.students.all()]

    class Meta:
        model = Course
        fields = ('id', 'name', 'department', 'department_id', 'students')

class DepartmentSerializer(serializers.ModelSerializer):
    # show courses under this department
    courses = CourseMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'courses')

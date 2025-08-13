from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def home(_):
    return HttpResponse("University API is running. Try /api/departments/")

urlpatterns = [
    path('', home),  # root page
    path('admin/', admin.site.urls),
    path('api/', include('university_app.urls')),
]



from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('student/',include('Myapp.urls')),
    path('student1/',include('App2.urls')),
    path('school/',include('app_School.urls')),
    path('dept/',include('app_Department.urls')),
    
]

from django.urls import path
from .views import *

urlpatterns=[
    path('teachperformance/',TeacherPerformanceView.as_view(),name='teachersperformance'),
    path('byid/<int:teacher_id>/',teacherdetailsView.as_view(),name='teacherdetails'),
    path('crud/',TeacherallDetailsView.as_view(),name='teachersalldetails'),
    path('updateperbyadd/',updateperbyaddView.as_view(),name='updateper'),
    path('performanceupdate/<int:rollno>/',performanceupdateView.as_view(),name='performanceupdate'),
    

]
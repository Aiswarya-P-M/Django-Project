from django.urls import path
from .views import *

urlpatterns=[
    path('teachperformance/',TeacherPerformanceView.as_view(),name='teachersperformance'),
    path('byid/<int:teacher_id>/',teacherdetailsView.as_view(),name='teacherdetails'),
    path('crud/',TeacherallDetailsView.as_view(),name='teachersalldetails'),
    path('updateperbyadd/',updateperbyaddView.as_view(),name='updateper'),
    path('performanceupdate/<int:rollno>/',performanceupdateView.as_view(),name='performanceupdate'),
    path('byschool/<int:sc_id>/',Teacherbyschoolview.as_view(),name='teacherbyschool'),
    path('activeteachers/',Activeteachers.as_view(),name='activeteachers'),
    path('inactiveteachers/', Inactiveteachers.as_view(), name='inactiveteachers'),
    path('teacherbydept/<int:dept_id>/',Teacherbydeptview.as_view(),name='teacherbydept'),
    path('u&d/<int:emp_id>/',TeacherbyidView.as_view(),name='teacherbyid')

]
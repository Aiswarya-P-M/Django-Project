from django.urls import path
from .views import *

urlpatterns=[
    path('',TeachercreateView.as_view(),name='createteacher'),
    path('byid/<int:emp_id>/',TeacherdetailsView.as_view(),name='teacherdetails'),
    path('teachperformance/',TeacherPerformanceView.as_view(),name='teachersperformance'),
    path('updateperbyadd/',UpdateperbyaddView.as_view(),name='updateper'),
    path('updateperbydel/<int:rollno>/',UpdateperbydelView.as_view(),name='performanceupdatebydel'),
    path('byschool/<int:sc_id>/',Teacherbyschoolview.as_view(),name='teacherbyschool'),
    path('activeteachers/',Activeteachers.as_view(),name='activeteachers'),
    path('inactiveteachers/', Inactiveteachers.as_view(), name='inactiveteachers'),
    path('teacherbydept/<int:dept_id>/',Teacherbydeptview.as_view(),name='teacherbydept'),
    path('teacherdeacivate/<int:emp_id>/',TeacherdeactivateView.as_view(),name='teacherdeactivate')

]
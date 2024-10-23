from django.urls import path
from .views import *

urlpatterns=[
    path('',Student1View.as_view(),name='list_student'),
    path('byid/<int:rollno>',Student1DetailView.as_view(),name='studentdetails_byid'),
    path('listoftoppers/',Student1Listtoppers.as_view(),name='studentlistoftoppers'),
    path('listofcutoffs/',Student1LitofcutoffsView.as_view(),name='studentlistofcutoffs'),
    path('listoffailed/',Student1ListofFailedView.as_view(),name='studentlistoffailed'),
    path('listofaverage/',Student1ListofaverageView.as_view(),name='studentlistofaverage'),
    path('subjectvice/',StudentsubjectwisefailedlistView.as_view(),name='subjectvicefailedlist'),
    path('teachperformance/',TeacherPerformanceView.as_view(),name='teachersperformance'),
    path('teacherdetails/<int:teacher_id>/',teacherdetailsView.as_view(),name='teacherdetails'),
    path('alldetails/',TeacherallDetailsView.as_view(),name='teachersalldetails'),
    path('updateperformance/',updateperformanceView.as_view(),name='updateper'),
    path('performanceupdate/<int:rollno>/',performanceupdateView.as_view(),name='performanceupdate'),
    

]
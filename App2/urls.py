from django.urls import path
from .views import *

urlpatterns=[
    path('',Student1View.as_view(),name='list_student'),
    path('student1byid/<int:rollno>',Student1DetailView.as_view(),name='studentdetails_byid'),
    path('studentlistoftoppers/',Student1Listtoppers.as_view(),name='studentlistoftoppers'),
    path('studentlistofcutoffs/',Student1LitofcutoffsView.as_view(),name='studentlistofcutoffs'),
    path('studentlistoffailed/',Student1ListofFailedView.as_view(),name='studentlistoffailed'),
    path('studentlistofaverage/',Student1ListofaverageView.as_view(),name='studentlistofaverage'),
    path('subjectvicefailedlist/',StudentsubjectwisefailedlistView.as_view(),name='subjectvicefailedlist'),
    path('teachersperformance/',TeacherPerformanceView.as_view(),name='teachersperformance'),

    

]
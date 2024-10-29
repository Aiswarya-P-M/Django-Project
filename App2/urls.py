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
    path('bydept/<int:dept_id>/',Studentbydeptactview.as_view(),name='studentbydeptactive'),
    path('byscid/<int:sc_id>/',StudentbyscidView.as_view(),name='studentbyscid'),
    path('stdunderteacher/<int:teacher_id>/',Studentunderteacher.as_view(),name='studetunderteacher'),
    path('studentbydept&sc/<int:dept_id>/<int:sc_id>/', Studentunderdeptandschool.as_view(), name='studentunderdeptandsc'),
    path('studentdeactivate/<int:rollno>/',StudentdeactivateView.as_view(),name='studentdeactivate'),
    path('activestudents/', ActivestudView.as_view(), name='activestudents'),
    path('inactivestudents/', InactivestudView.as_view(), name='inactivestudents'),
    

]
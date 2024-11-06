from django.urls import path
from .views import *

urlpatterns=[
    path('',UsercreateView.as_view(),name='create_user'),
    path('reset_pswd/',ChangePasswordView.as_view(),name='reset_password'),
    path('login/', LoginView.as_view(), name='login')
    
    

]
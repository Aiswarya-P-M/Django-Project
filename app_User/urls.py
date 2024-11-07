from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('',UsercreateView.as_view(),name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('byid/<int:id>/', UserOperationByID.as_view(), name='user_by_id'),
    
    
    

]
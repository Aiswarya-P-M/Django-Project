from django.urls import path
from .views import *

urlpatterns=[
    path('',DeptcreateView.as_view(),name='create_department'),
    path('byid/<int:dept_id>',DeptdetailsView.as_view(),name='department_details')
]
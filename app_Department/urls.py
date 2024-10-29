from django.urls import path
from .views import *

urlpatterns=[
    path('',DeptcreateView.as_view(),name='create_department'),
    path('byid/<int:dept_id>',DeptdetailsView.as_view(),name='department_details'),
    path('deactivatedept/<int:dept_id>', DeptdeactivateView.as_view(), name='deactivate_department'),
    path('activedept/',ActivedeptView.as_view(),name='active_department'),
    path('inactivedept/',InactiveDeptView.as_view(),name='inactive_department')
]
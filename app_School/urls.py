from django.urls import path
from .views import *

urlpatterns=[
    path('',SchoolcreateView.as_view(),name='create_school'),
    path('byid/<int:sc_id>',SchooldetailsView.as_view(),name='school_details')
]
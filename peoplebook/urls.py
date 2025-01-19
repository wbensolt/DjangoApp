from django.urls import path

from apptwo.urls import urlpatterns
from . import views

urlpatterns = [
    path('users/', views.users_list),
    path('users/<str:display>/', views.users_list),
    path('users/<str:name>/detail/', views.users_detail, name='peoplebook-users-detail'),
]
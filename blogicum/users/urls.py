from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('<str:username>/', views.ProfileListView.as_view(), name='profile'),
    path('<str:username>/edit/', views.ProfileUpdateView.as_view(), name='edit_profile'),
]

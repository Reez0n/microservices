from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    path('<int:post_id>/add/', views.add_comment, name='add_comment'),
    path('<int:post_id>/edit/<int:comment_pk>/', views.edit_comment, name='edit_comment'),
    path('<int:post_id>/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]

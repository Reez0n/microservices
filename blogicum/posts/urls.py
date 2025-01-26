from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    path('category/<slug:category_slug>/', views.CategoryListView.as_view(), name='category_posts'),
]

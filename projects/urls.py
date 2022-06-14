from django.urls import path
from .views import UserPictureListView, ProjectCreateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_post, name='search'),
    path('project/new/', ProjectCreateView.as_view(), name='project-new'),
    path('user/<str:username>/projects/', UserPictureListView.as_view(), name='user-posts'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]
from django.urls import path
from .views import UserPictureListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_post, name='search'),
    path('user/<str:username>/projects/', UserPictureListView.as_view(), name='user-posts'),
    path('detail/<str:title>/', views.detail, name='detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_post, name='search'),
    path('detail/<str:pk>', views.detail, name='detail'),
]
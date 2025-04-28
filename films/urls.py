from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),  # Детальная страница фильма
]

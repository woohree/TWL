from django.urls import path
from . import views

app_name = 'practice'

urlpatterns = [
  path('', views.article_list, name='article_list'),
  path('<int:article_pk>/', views.article_detail, name='article_detail'),
]
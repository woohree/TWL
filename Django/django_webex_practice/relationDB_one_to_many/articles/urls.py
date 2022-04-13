from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('<int:article_pk>/', views.detail, name='detail'),
]

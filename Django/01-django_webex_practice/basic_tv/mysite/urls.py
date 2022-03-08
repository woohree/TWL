from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
  # /mysite/
  path('', views.home),
  path('lunch/', views.lunch, name='lunch'),
  # /mysite/lotto/
  path('lotto/', views.lotto, name='lotto'),
  # /mysite/greeting/woohree => variable routing!
  path('greeting/<str:name>/', views.greeting)
]

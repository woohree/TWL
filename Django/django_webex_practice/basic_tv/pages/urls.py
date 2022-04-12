from django.urls import path
from . import views


urlpatterns = [
  path('dinner/<str:menu>/<int:number>/', views.dinner),
  # /pages/check/
  path('check/', views.check)
]
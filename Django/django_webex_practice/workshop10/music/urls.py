from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.artist_index_create),
    path('artists/<int:artist_pk>/', views.artist_detail),
    path('artists/<int:artist_pk>/music/', views.music_create),
    path('music/', views.music_index),
    path('music/<int:music_pk>/', views.music_detail_update_delete),
]

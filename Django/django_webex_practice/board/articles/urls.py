from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_read, name='read'),
    
    # 새 게시글
    path('new/', views.article_new, name='new'),
    path('create/', views.article_create, name='create'),

    path('<int:pk>/', views.article_detail, name='detail'),

    path('<int:pk>/delete/', views.article_delete, name='delete'),

    # 수정
    path('<int:pk>/edit/', views.article_edit, name='edit'),
    path('<int:pk>/update/', views.article_update, name='update'),
]

from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:username>', views.profile, name='profile'),  # str은 안써도됨, 기본값이라

    # 오늘 이후로 아마 안쓴다고 함
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.change_pw, name='change_pw'),
]

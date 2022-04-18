from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<str:username>/', views.profile, name='profile'),  # url이 문자열로 시작하는 경우, 가장 아래에 둘 수 있도록!!! 안그러면, 다른 url을 다 먹음!!!
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]

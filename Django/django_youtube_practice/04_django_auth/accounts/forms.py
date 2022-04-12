from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):

    password = None  # 패스워드 어쩌고 하는 내용 없애기 => UserChangeForm 들어가서 보면 인자가 보임, 그거 없애버린것 => 비번 바꾸는 링크 새로 삽입해줘야함

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
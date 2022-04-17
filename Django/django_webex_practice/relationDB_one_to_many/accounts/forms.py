from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(UserCreationForm):

    # age = forms.IntegerField(min_value=12, max_value=150, required=False)

    class Meta:
        model = User
        # UserCreationForm에는 'username' 필드만 있음
        fields = UserCreationForm.Meta.fields #+ ('first_name', 'last_name', 'age',)
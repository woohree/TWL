from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'name',
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'phone',
            }
        )
    )
    is_cs = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'cs',
            }
        ),
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'age',
            }
        )
    )


    class Meta:
        model = Student
        fields = '__all__'
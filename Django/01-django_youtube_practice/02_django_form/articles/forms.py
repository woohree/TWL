from .models import Article
from django import forms


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'my_class class_two',    # 스타일 만지기 위해, 클래스 생성
                'placeholder': 'Enter the title', # 디폴트 입력 값
            }
        )
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my_content',            # 클래스 생성

            }
        ),  # <<< 쉼표 주의!!
        error_messages={                          # 에러 메시지 수정
            'required': 'Please enter content!!',
        }
    )

    class Meta:
        model = Article
        fields = '__all__'


# class ArticleForm(forms.Form):
#     REGION_A = 'sl'             # value
#     REGION_B = 'dj'
#     REGION_C = 'gj'
#     REGIONS_CHOICES = [
#         (REGION_A, '서울'),     # 출력
#         (REGION_B, '대전'),
#         (REGION_C, '광주'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=REGIONS_CHOICES)
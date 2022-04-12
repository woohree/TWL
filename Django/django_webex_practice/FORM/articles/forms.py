from django import forms
from articles.models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=2, max_length=10)
    class Meta:
        model = Article
        fields = '__all__'
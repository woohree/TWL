from django.shortcuts import get_object_or_404, render
from .models import Article


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
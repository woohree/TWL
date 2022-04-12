from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
    # db의 모든 article 목록 조회
    datas = Article.objects.all()
    context = {
      'datas': datas,
    }
    return render(request, 'practice/article_list.html', context)


def article_detail(request, article_pk):
    # db의 pk=article_pk 인 article 조회
    data = Article.objects.get(pk=article_pk)
    context = {
      'data': data,
    }
    return render(request, 'practice/article_detail.html', context)

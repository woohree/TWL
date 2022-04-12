from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def article_read(request):
    # articles = Article.objects.all()  # 오름차순
    articles = Article.objects.all().order_by('-pk')  # 내림차순(pk값은 변경가능)
    context = {
      'articles': articles,
    }
    return render(request, 'articles/article_read.html', context)

# 글 작성 버튼을 누르면 /articles/new/
# form 제공
# form 제출 시 /articles/create/
def article_create(request):
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return redirect('articles:detail', article.pk)


def article_new(request):
    return render(request, 'articles/article_new.html')


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
      'article': article,
    }
    return render(request, 'articles/article_detail.html', context)


def article_edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
      'article': article,
    }
    return render(request, 'articles/article_edit.html', context)


def article_update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return redirect('articles:detail', article.pk)


def article_delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:read')
    elif request.method == 'GET':
        return redirect('articles:detail', article.pk)
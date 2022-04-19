from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@require_safe
def article_index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article_index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:article_detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/article_form.html', context)


@login_required
@require_safe
def article_detail(request, article_pk):
    is_like = request.user.like_articles.filter(pk=article_pk).exists()
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    context = {
        'article': article,
        'form': form,
        'is_like': is_like,
    }
    return render(request, 'articles/article_detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:article_detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form,
            'article': article,
        }
        return render(request, 'articles/article_form.html', context)
    return redirect('articles:article_detail', article.pk)


@login_required
@require_POST
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:article_index')


@login_required
@require_POST
def comment_create(request, article_pk):
    form = CommentForm(request.POST)
    article = get_object_or_404(Article, pk=article_pk)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = article
        comment.save()
    return redirect('articles:article_detail', article.pk)


@login_required
@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    article = get_object_or_404(Article, pk=article_pk)  # 검증차원에서 필요
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:article_detail', comment.article.pk)


@login_required
@require_POST
def article_like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.like_articles.filter(pk=article_pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:article_detail', article.pk)
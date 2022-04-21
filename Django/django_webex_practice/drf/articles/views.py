from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer


@api_view(['GET', 'POST',])
def article_index_create(request):

    def article_index():
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def article_create():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


    if request.method == 'GET':
        return article_index()

    elif request.method == 'POST':
        return article_create()


@api_view(['GET', 'PUT', 'DELETE',])
def article_detail_update_delete(request, article_pk):

    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def article_update():
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def article_delete():
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        return article_detail()
    
    elif request.method == 'PUT':
        return article_update()

    elif request.method == 'DELETE':
        return article_delete()


@api_view(['POST',])
def comment_create(request, article_pk):

    def comment_create():
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data)


    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        return comment_create()


@api_view(['PUT', 'DELETE',])
def comment_update_delete(request, article_pk, comment_pk):
    
    def comment_update():
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def comment_delete():
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        return comment_update()

    elif request.method == 'DELETE':
        return comment_delete()
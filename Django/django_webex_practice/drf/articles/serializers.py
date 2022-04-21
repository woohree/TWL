from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class CommentListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)

    title = serializers.CharField(min_length=2, max_length=100)
    content = serializers.CharField(min_length=10)
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'comments', 'created_at', 'updated_at',)


class ArticleListSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Article
        fields = ('title', 'updated_at', 'comments_count',)


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', 'content', 'article',)
        read_only_fields = ('article',)

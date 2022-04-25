from rest_framework import serializers
from ..models import Card
# from .article import ArticleListSerializer


class CardSerializer(serializers.ModelSerializer):
    # articles = ArticleListSerializer(many=True, read_only=True)
    class Meta:
        model = Card
        fields = '__all__'
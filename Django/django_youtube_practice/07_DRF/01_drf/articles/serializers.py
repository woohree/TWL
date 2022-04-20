from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)  # 읽기전용 필드, 유효성 검사는 안하되, 결과에는 포함됨


class ArticleSerializer(serializers.ModelSerializer):
    # Meta fields 안에 없는 값은 따로 읽기전용 설정이 필요 / 있는 값은 Meta에서 설정!

    # # 이름바꾸려면, 원래 모델에서 related_name 설정 후, 그 이름으로 설정하면 됨 => pk값만 출력
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  

    # 중첩된 관계 표현(1:N에서 사용) => 정보 전부 출력
    comment_set = CommentSerializer(many=True, read_only=True)

    # 조회한 게시글의 댓글 수 출력, article.comment_set.count()
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

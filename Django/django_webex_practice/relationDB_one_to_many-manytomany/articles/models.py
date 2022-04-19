from django.db import models
from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=100)
    content = models.TextField()

    @classmethod
    def seed_data(cls, n):
        from faker import Faker
        f = Faker()
        for _ in range(n):
            cls.objects.create(
                title = f.paragraph(),
                content = f.paragraph(10),
                user_id = 4,
            )
        # shell_plus켜서 Article.seed_data(#) 해서 더미 데이터 생성 가능


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    content = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}> {self.content}'
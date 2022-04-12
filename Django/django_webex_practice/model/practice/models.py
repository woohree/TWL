from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    is_married = models.BooleanField(default=False)


class Article(models.Model):
    title = models.CharField(max_length=200)
    artist = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lyrics = models.TextField(default='')

    def __str__(self):
        return f'{self.pk}번 Title) {self.title}'
from tkinter import CASCADE
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(models.Model):
    content = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}> {self.content}'
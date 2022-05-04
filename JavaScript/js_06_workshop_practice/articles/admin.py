from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    exclude = ('like_users',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

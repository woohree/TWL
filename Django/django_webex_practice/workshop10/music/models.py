from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

  
class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musics')
    title = models.CharField(max_length=200)
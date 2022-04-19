from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')  # symmetrical이 True면, 맞팔이 자동으로됨, False면, 맞팔 자동x


    def get_rank(self):
        fan_count = self.followers.count()
        if fan_count > 100:
            rank = 1
        elif fan_count > 50:
            rank = 2
        else:
            rank = 3
        return rank
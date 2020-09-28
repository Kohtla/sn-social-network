from django.db import models
from users.models import User

class Post(models.Model):
    name = models.CharField(max_length=100, verbose_name='Post name')
    content = models.TextField(verbose_name='Content text')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.name
    
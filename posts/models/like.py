from django.db import models

from .post import Post
from users.models import User


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
    
    def __str__(self):
        return '%s - %s'%(self.post, self.user)

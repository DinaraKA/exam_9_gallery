from django.contrib.auth.models import User
from django.db import models

class Photo(models.Model):
    photo = models.ImageField(upload_to='user_pics', verbose_name='Photo')
    note = models.CharField(max_length=50, verbose_name='Note')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Added date")
    like = models.IntegerField(default=0, verbose_name='Like')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name='Added by')

    def __str__(self):
        return self.note

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


class Comment(models.Model):
    text = models.TextField(max_length=200, verbose_name='Comment')
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, verbose_name='Photo', related_name='photo_comment')
    comment_author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name='Added by')
    comment_created_at = models.DateTimeField(auto_now_add=True, verbose_name="Added date")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

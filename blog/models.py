from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=u"Название поста")
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        verbose_name = u"Пост"
        verbose_name_plural = u"Посты"

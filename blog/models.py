from django.db import models
from django.urls import reverse
from django.utils import timezone


class Blog(models.Model):
    author = models.ForeignKey('auth.User', related_name='blogger', on_delete=models.CASCADE, verbose_name=u"Автор блога")
    title = models.CharField(max_length=255, verbose_name=u"Название блога")
    description = models.CharField(max_length=1024, verbose_name=u"Описание блога")
    pub_date = models.DateTimeField(default=timezone.now, verbose_name=u"Дата создания блога")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

    class Meta:
        verbose_name = u"Блог"
        verbose_name_plural = u"Блоги"
        ordering = ('pub_date', )


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=u"Автор поста")
    title = models.CharField(max_length=255, verbose_name=u"Название поста")
    blog = models.ForeignKey(Blog, related_name='blogs', on_delete=models.CASCADE)
    body = models.TextField(verbose_name=u"Текст поста")
    create_date = models.DateTimeField(default=timezone.now, verbose_name=u"Дата создания поста")
    update_date = models.DateTimeField(auto_now=True, verbose_name=u"Дата последнего редактирования поста")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.blog.id), str(self.id)])

    class Meta:
        verbose_name = u"Пост"
        verbose_name_plural = u"Посты"


class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=u"Автор комментария")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField(verbose_name=u"Текст")
    create_date = models.DateTimeField(default=timezone.now, verbose_name=u"Дата создания")

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('comment_detail', args=[str(self.post.blog.id), str(self.post.id), str(self.id)])

    class Meta:
        verbose_name = u"Комментарий"
        verbose_name_plural = u"Комментарии"
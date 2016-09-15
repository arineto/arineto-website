from django.db import models
from apps.blog.managers import PostQuerySet


class Tag(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):

    post = models.ForeignKey('blog.Post')
    author = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    website = models.URLField(null=True, blank=True, verbose_name='Website')
    content = models.TextField(verbose_name='Message')
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return '{0} - {1}'.format(self.author, self.post)


class Post(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()

    tags = models.ManyToManyField('blog.Tag')

    created_at = models.DateTimeField(auto_now_add=True)
    released_at = models.DateTimeField(blank=True, null=True)
    released = models.BooleanField(default=False)

    objects = PostQuerySet.as_manager()

    class Meta:
        ordering = ['-released_at']

    def __str__(self):
        return '{0} - {1}'.format(
            self.created_at.strftime('%d/%m/%Y'),
            self.title
        )

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Manager
from django.utils import timezone


class PostedManager(Manager):
    def get_queryset(self):
        return super(PostedManager, self).get_queryset().filter(status='posted')


class Post(models.Model):

    STATUS_CHOICES = (
        ('Published', 'published'),
        ('Draft', 'draft')
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    under_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    posted = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    objects = models.Manager()
    published = PostedManager()

    class Meta:
        ordering = ('-posted',)

    def __str__(self):
        return self.title

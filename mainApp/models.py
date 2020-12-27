from django.db import models
from django.contrib.auth.models import User
from django.db.models import Manager
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager


class PostedManager(Manager):
    def get_queryset(self):
        return super(PostedManager, self).get_queryset().filter(status='posted')


class Post(models.Model):
    tags = TaggableManager()

    STATUS_CHOICES = (
        ('posted', 'Posted'),
        ('draft', 'Draft'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    under_title = models.CharField(max_length=255, blank=True, null=True, default='_')
    image = models.ImageField(upload_to='media', blank=True, null=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()
    posted = PostedManager()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.posted.year, self.posted.month,
                                            self.posted.day, self.posted.slug])


class Project(models.Model):

    STATUS_CHOICES = (
        ('posted', 'Posted'),
        ('draft', 'Draft'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    under_title = models.CharField(max_length=255, blank=True, null=True, default="  ")
    image = models.ImageField(upload_to='media', blank=True, null=True)
    text = models.TextField()

    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()
    posted = PostedManager()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.posted.year, self.posted.month,
                                            self.posted.day, self.posted.slug])

    # def get_absolute_url(self):
    #     return reverse('blogApp:post_detail', args=[self.published.year, self.published.month,
    #                                                 self.published.day, self.slug])

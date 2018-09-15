from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


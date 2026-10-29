from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.URLField(max_length=200, blank=True)

    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

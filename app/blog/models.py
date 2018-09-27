from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    auther = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    titie = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    publishied_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishied_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titie
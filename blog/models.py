from django.db import models
from django.conf import settings
from django.utils import timezone

class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
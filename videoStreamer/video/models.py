from django.db import models
from accounts.models import User

class Video(models.Model):
    name = models.CharField(max_length=255)
    uloaded_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/')
    url = models.URLField()
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.name

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='image/', height_field=None, width_field=None, max_length=100,
                              verbose_name='image')
    likes = models.ManyToManyField(User, related_name='likes')

    def get_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.name


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post_for = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'Comment for post: {self.post_for.name}. From: {self.owner.name}'

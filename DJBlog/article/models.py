from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    cate_name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.cate_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=16, null=True)
    author = models.ForeignKey(User, related_name='posts')

    def __str__(self):
        return self.title

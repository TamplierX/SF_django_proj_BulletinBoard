from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

from .resources import CATEGORY_TYPE


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=5, choices=CATEGORY_TYPE, default="TANKS")
    date_create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    content = RichTextUploadingField()

    def __str__(self):
        return f'''{self.pk} | {self.date_create.strftime("%d.%m.%Y %H:%M")} | {self.author} 
        | {self.title[0:15]} | {self.content[0:15]}'''

    def get_absolute_url(self):
        return reverse('post_details', args=[str(self.pk)])


class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} | {self.date_create} | {self.author} | {self.text[0:25]}'

    def get_absolute_url(self):
        return reverse('response_detail', args=[str(self.pk)])

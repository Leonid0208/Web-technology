from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey('auth.User')
    likes = models.ManyToManyField(User, related_name='likes_set')

    def __str__(self):
        return self.title

    def get_url(self):
        return 'question/{}/'.format(self.id)


class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateField(null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.text

from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        post = Question(**self.cleaned_data)
        post.author_id = self._user.id
        post.save()
        return post


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        pass

    def save(self):
        post = Answer(**self.cleaned_data)
        post.author_id = self._user.id
        post.save()
        return post


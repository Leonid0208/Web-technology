from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator
from .models import Question


def question(request):
    posts = Question.objects.all().order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(posts, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'list.html',
                  {'title': 'Latest',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,
                   'user': request.user,
                   'session': request.session, })


def question_famous(request):
    posts = Question.objects.all().order_by('-rating')
    page = request.GET.get('page')
    paginator = Paginator(posts, 10)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'list.html',
                  {'title': 'Latest',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,
                   'user': request.user,
                   'session': request.session, })


def found(request):
    return HttpResponse("Found!")


def not_found(request):
    return HttpResponseNotFound("Not Found!")




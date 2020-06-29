from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# def test(request, *args, **kwargs):
#     return render(request, 'qa/qa.html', {})
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def not_found(request):
    return HttpResponseNotFound('Not found!')
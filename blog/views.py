from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


def main(request):
    return HttpResponse('<h1>Hello world</h1>')


def test(request):
    return render(request, 'ders1.html', {})

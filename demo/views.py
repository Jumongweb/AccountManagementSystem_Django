from django.shortcuts import render, HttpResponse


# Create your views here.
# localhost:8000/demo/hello


def say_hello(request):
    return HttpResponse("Hello world")


def welcome(request, name):
    return render(request, 'index.html', {"name": name})
from django.shortcuts import render
from django.http import HttpResponse


def Hello_world(request):
    return HttpResponse("Hello World!!")


def index(request):
    return render(request, "index.html")


def base_test(request):
    return render(request, "base.html")

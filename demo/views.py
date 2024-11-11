from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(
        "<h1 style='background-color:skyblue;display:flex;justify-content:center;'>Hello, code runner.</h1>")


def inspect_request(request):
    return render(request, 'demo/index.html', context=dict(request=request))

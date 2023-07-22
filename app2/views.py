from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("<h1>This is second app first line</h1>")


def second(request):
    return HttpResponse("<h1>This is second app second line</h1>")


from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    alireza_string= "Hello, world. You're at the alireza index."
    return HttpResponse(alireza_string)
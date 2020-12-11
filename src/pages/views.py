from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home_views(request, *args, **kwargs):
    print(request)
    print(request.user)
    return HttpResponse("<h1> Hellow World </h1>")

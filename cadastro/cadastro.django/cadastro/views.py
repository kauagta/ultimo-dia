from django.shortcuts import render
from setup import urls

def base(request):
    return render(request, 'base.html')
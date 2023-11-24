from django.http import HttpResponse
from django.shortcuts import render
from setup import urls

def pagina1(request):
    return render(request, 'pagina1.html')

def pagina2(request):
    return render(request, 'pagina2.html')

def pagina3(request):
    return render(request, 'pagina3.html')

def pagina1(request):
    return render(request, 'pagina1.html')





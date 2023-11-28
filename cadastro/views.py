from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from .models import Usuario


def pagina1(request):
    return render(request, 'pagina1.html')

def pagina2(request):
    return render(request, 'pagina2.html')

def pagina3(request):
    usuario = request.POST.get('nome')    
    usuario = request.POST.get('idade')
    usuario.save()
    
    Usuario = {
       'usuario': usuario.objects.all()
    }
    return render(request, 'pagina3.html', Usuario)



from django.contrib import admin
from django.urls import path
from cadastro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina1, name='pagina1'),
    path('pagina2.html', views.pagina2, name='pagina2'),  
    path('pagina3.html', views.pagina3, name='pagina3'),
]

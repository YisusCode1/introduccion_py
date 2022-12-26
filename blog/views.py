from django.shortcuts import render
from django.views.generic import View
#importando el formulario creado
from .forms import PostCreateForm

# Create your views here.
#creando la vista del indice donde vamos a enlistar todos los post que existen

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request,'blog_list.html', context)
    
#vamos a crear una nueva vista llamada

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'blog_create.html', context)
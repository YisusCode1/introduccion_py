from django.shortcuts import render
from django.views.generic import View

# Create your views here.
#creando la vista del indice donde vamos a enlistar todos los post que existen

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request,'blog_list.html', context)
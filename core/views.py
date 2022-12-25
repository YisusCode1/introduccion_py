from django.views.generic import View
from django.shortcuts import render

#cuando trabajemos con una class usemos self
class HomeView(View):
    def get(self, request, *args, **kwargs):
        # context esto es un diccionario
        context={
            
        }
        #o puedes poner {} en vez de context es lo mismo
        # '' es un temple es importante para ver la informacion
        return render(request, 'index.html',context)
from django import forms

#traemos el modelo que queremos manipular

from .models import Post

#vamos a declarar el formulario

class PostCreateForm(forms.ModelForm):
    #dentro de meta declaramos el modelo que queremos editar para este formulario
    class Meta:
        model=Post
        fields=('title','content')
        
#ahora el formulario lo llevamos a views
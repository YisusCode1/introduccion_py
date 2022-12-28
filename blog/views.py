from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, UpdateView, DeleteView
#importando el formulario creado
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
#creando la vista del indice donde vamos a enlistar todos los post que existen

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all() #llamando todos los posts
        context={
            'posts':posts # pasando la variable que contiene la info a 'posts
        }
        return render(request,'blog_list.html', context)
    
#vamos a crear una nueva vista llamada

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        
        context={
            'form':form
        }
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
                form = PostCreateForm(request.POST)
                if form.is_valid():
                    title = form.cleaned_data.get('title')
                    content = form.cleaned_data.get('content')
                    
                    p, created = Post.objects.get_or_create(title=title, content=content)
                    p.save()
                    return redirect('blog:home')
        context={
            
        }
        return render(request, 'blog_create.html', context)
    
class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context={
            'post':post
        }
        return render(request, 'blog_detail.html', context)

#actualizar una vista   
class BlogUpdateView(UpdateView):
    #que modelo queremos editar pues el post
    model=Post
    fields=['title', 'content']
    template_name='blog_update.html'
    
    def get_success_url(self):
        pk =self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})
    
#borrando una vista

class BlogDeleteView(DeleteView):
    model=Post
    template_name='blog_delete.html'
    success_url= reverse_lazy('blog:home')

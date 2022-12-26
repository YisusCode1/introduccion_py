from django.db import models

# Create your models here.
#CharField es un campo de caracteres
#en max_length le podemos dar el numero que querramos
class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    
    def __str__(self):
        return self.title
#terminando empezamos a migrar la informacion
#self hace referencia al post y le dara el nombre de titulo que le dimos

#creando un url basico para poder acceder a todas las vistas que estamos por crear de nuestro blog
#y estamos conectando al url de core
from django.urls import path
from .views import BlogListView

app_name="blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home")
]

from django.contrib import admin
from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    #se ha reescrito la vista anterior
    path('', HomeView.as_view(), name="home"),
    #incluyendo nombre blog.urls y que nombre le damos blog
    path('blog/',include('blog.urls', namespace='blog'))
]


from django.contrib import admin
from django.urls import path, include
from aluraflix.views import VideoViewSet,Categoria1ViewSet,ListaVideoPorCategoria,ListaVideosFree
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos',VideoViewSet,basename='videos')
router.register('categorias',Categoria1ViewSet,basename='Categorias')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/free/',ListaVideosFree.as_view()),
    path('',include(router.urls)),
    path('categorias/<int:pk>/videos',ListaVideoPorCategoria.as_view()),
    
]
#ANOTACION IMPORTANTE: LAS URL TIENEN QUE IT EN ORDEN DE MAS IMPORTANTE A MENOS IMPORTANTE, tenia un error a la hora de accesar la url porque buscaba primero videos y ahi se estancaba.
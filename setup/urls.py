
from django.contrib import admin
from django.urls import path, include
from aluraflix.views import VideoViewSet,Categoria1ViewSet,ListaVideoPorCategoria,ListaVideosFree
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos',VideoViewSet,basename='videos')
router.register('categorias',Categoria1ViewSet,basename='Categorias')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('categorias/<int:pk>/videos',ListaVideoPorCategoria.as_view()),
    path('videos/free',ListaVideosFree.as_view())
]

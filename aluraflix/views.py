from aluraflix.models import Video,Categoria1
from aluraflix.serializers import VideoSerializer,Categoria1Serializer, ListaVideosPorCategoriaSerializer
from rest_framework import viewsets,filters,generics
from django_filters.rest_framework import DjangoFilterBackend

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    search_fields =['id']

class Categoria1ViewSet(viewsets.ModelViewSet):
    queryset=Categoria1.objects.all()
    serializer_class=Categoria1Serializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    search_fields =['id']

class ListaVideoPorCategoria(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(categoria = self.kwargs['pk'])
        return queryset
    serializer_class =ListaVideosPorCategoriaSerializer
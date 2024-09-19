from aluraflix.models import Video,Categoria1
from aluraflix.serializers import VideoSerializer,Categoria1Serializer, ListaVideosPorCategoriaSerializer,ListaVideosFreeSerializer
from rest_framework import viewsets,filters,generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed



class CustomBasicAuthentication(BasicAuthentication):
    def authenticate(self, request):
        user_auth = super().authenticate(request)
        if not user_auth:
            raise AuthenticationFailed(detail="Credenciales no válidas. Por favor, verifique su usuario y contraseña.")
        return user_auth
    

class VideoViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomBasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    search_fields =['id']

class Categoria1ViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomBasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Categoria1.objects.all()
    serializer_class=Categoria1Serializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    search_fields =['id']

class ListaVideoPorCategoria(generics.ListAPIView):
    authentication_classes = [CustomBasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Video.objects.filter(categoria = self.kwargs['pk'])
        return queryset
    serializer_class =ListaVideosPorCategoriaSerializer

class ListaVideosFree(generics.ListAPIView):
   
    def get_queryset(self):
       queryset =Video.objects.filter(free=True)
       return queryset
    serializer_class = ListaVideosFreeSerializer
    

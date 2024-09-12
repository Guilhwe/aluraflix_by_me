from aluraflix.models import Video
from aluraflix.serializers import VideoSerializer
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    search_fields =['id']
   
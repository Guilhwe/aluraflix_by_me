from aluraflix.models import Video
from aluraflix.serializers import VideoSerializer
from rest_framework import viewsets

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

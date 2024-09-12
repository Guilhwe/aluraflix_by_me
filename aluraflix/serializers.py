from rest_framework import serializers
from aluraflix.models import Video,Categoria1

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields ='__all__'  
    
class  Categoria1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria1 
        fields ='__all__'  
        
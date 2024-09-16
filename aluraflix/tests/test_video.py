from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from aluraflix.models import Video,Categoria1
from aluraflix.serializers import VideoSerializer

class VideosTestCase(APITestCase):
    def setUp(self):
        categoria_ejemplo = Categoria1.objects.create(nombre='1',color='rosa')
        self.usuario= User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('videos-list')
        self.client.force_authenticate(user=self.usuario)
        self.video_01 = Video.objects.create(
            titulo = 'TITULO TEST 1',
            description = 'EJEMPLO1',
            url = 'https://www.ejemplo1.com',
            categoria = categoria_ejemplo
        )
        self.video_02 = Video.objects.create(
            titulo = 'TITULO TEST 2',
            description = 'EJEMPLO2',
            url = 'https://www.ejemplo2.com',
            categoria = categoria_ejemplo
        )
    
    def test_get_para_listar_videos(self):
        '''Test para la requisicion GET'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_get_para_listar_un_video(self):
        '''Test para la requisicion GET de un video'''
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        datos_video = Video.objects.get(pk=1)
        datos_video_serializados = VideoSerializer(instance=datos_video).data
        self.assertEqual(response.data,datos_video_serializados)
    
    def test_post_para_crear_un_video(self):
        '''Test para la requisicion POST de un video'''
        datos ={
            'titulo':'test',
            'description':'test',
            'url':'https://www.ejemplo3.com',
            'categoria':'1',
        }
        response = self.client.post(self.url,datos)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_post_para_BORRAR_un_video(self):
        '''Test para la requisicion DELETE de un video'''
        respose = self.client.delete(self.url+'1/')
        self.assertEqual(respose.status_code,status.HTTP_204_NO_CONTENT)
    
    def test_post_para_actualizar_un_video(self):
        '''Test para la requisicion PUT/PATCH de un video'''
        datos ={
            'titulo':'test',
            'description':'testpatch',
            'url':'https://www.ejemplo3.com',
            'categoria':'1',
        }
        respose = self.client.patch(self.url+'2/')
        self.assertEqual(respose.status_code,status.HTTP_200_OK)
    
    
    
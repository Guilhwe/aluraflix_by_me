from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from aluraflix.models import Video,Categoria1
from aluraflix.serializers import Categoria1Serializer

class CategoriasTestCase(APITestCase):
    def setUp(self):
        self.usuario= User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Categorias-list')
        self.client.force_authenticate(user=self.usuario)
        self.categoria_01 = Categoria1.objects.create(
            nombre = 'CatEj1',
            color = 'EJEMPLO1',
            
        )
        self.categoria_02 = Categoria1.objects.create(
            nombre = 'CatEj2',
            color = 'EJEMPLO2',
            
        )
    
    def test_get_para_listar_categorias(self):
        '''Test para la requisicion GET'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_get_para_listar_una_categoria(self):
        '''Test para la requisicion GET de una categoria'''
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        datos_categoria = Categoria1.objects.get(pk=1)
        datos_categoria_serializados = Categoria1Serializer(instance=datos_categoria).data
        self.assertEqual(response.data,datos_categoria_serializados)
    
    def test_post_para_crear_una_categoria(self):
        '''Test para la requisicion POST de una categoria'''
        datos ={
            'nombre':'test',
            'color':'test1',
            
        }
        response = self.client.post(self.url,datos)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_post_para_BORRAR_una_categoria(self):
        '''Test para la requisicion DELETE de una categoria'''
        respose = self.client.delete(self.url+'2/')
        self.assertEqual(respose.status_code,status.HTTP_204_NO_CONTENT)
    
    def test_post_para_actualizar_una_categoria(self):
        '''Test para la requisicion PUT/PATCH de un video'''
        datos ={
            'nombre':'test',
            'color':'testpatch',
            
        }
        respose = self.client.patch(self.url+'2/')
        self.assertEqual(respose.status_code,status.HTTP_200_OK)
from django.test import TestCase
from aluraflix.models import Video,Categoria1

class ModelVideoTestCase(TestCase):
   
    # def test_fallido(self):
    #     self.fail('Test Fallido')
    def setUp(self):
        categoria_ejemplo = Categoria1.objects.create(nombre='1',color='rosa')
        self.video =Video.objects.create(
            titulo = 'TITULO TEST',
            description = 'EJEMPLO',
            url = 'https://www.ejemplo.com',
            categoria = categoria_ejemplo
        )
    def test_comprueba_atributos_video(self):
        '''test que verifica los atributos del modelo de Video'''
        self.assertEqual(self.video.titulo,'TITULO TEST')

    
class ModelCategoriaTestCase(TestCase):
    def setUp(self):
        self.categoria=Categoria1.objects.create(
            nombre='ejemplo',
            color='ejemplo'
        )
    def test_comprueba_atributos_categoria(self):
        '''test que verifica los atributos de la categoria'''
        self.assertEqual(self.categoria.nombre,'ejemplo')
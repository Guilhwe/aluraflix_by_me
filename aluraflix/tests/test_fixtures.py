from django.test import TestCase
from aluraflix.models import Video, Categoria1

class FixturesTestCase(TestCase):
    fixtures = ['banco.json']

    def test_load_fixtures(self):
        '''Test para verificar la fixtures'''
        video =Video.objects.get(pk=2)
        categoria = Categoria1.objects.get(pk=1)
        self.assertEqual(video.url,"https://www.youtube.com/watch?v=weQ8ssA6iBU")
        self.assertEqual(categoria.color,'azul')
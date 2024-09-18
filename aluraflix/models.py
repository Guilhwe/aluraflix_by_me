from django.db import models

class Categoria1(models.Model):
    nombre = models.CharField(max_length=15, null=False, blank=False)
    color = models.CharField(max_length=10,null=False,blank=False)
    def __str__(self):
        return self.nombre

class Video(models.Model):


    titulo = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=300, null=False, blank=False)
    url = models.URLField(max_length = 50, null=False, blank=False )
    categoria = models.ForeignKey(Categoria1, on_delete=models.SET_DEFAULT,null=False,default=1)
    free = models.BooleanField(blank=False,null=False,default=False)

    def __str__(self):
        return self.titulo
    
  

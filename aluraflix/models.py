from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=300, null=False, blank=False)
    url = models.URLField(max_length = 50, null=False, blank=False )

    def __str__(self):
        return self.titulo
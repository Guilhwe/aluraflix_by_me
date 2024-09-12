from django.contrib import admin
from aluraflix.models import Video,Categoria1

class Videos(admin.ModelAdmin):
    list_display = ('id','titulo','description','url',)
    list_display_links =('id','titulo',)
    list_per_page = 5
    search_fields = ('id','titulo')
admin.site.register(Video,Videos)

class Categorias(admin.ModelAdmin):
    list_display = ('id','nombre','color')
    list_display_links=('id','nombre')

admin.site.register(Categoria1,Categorias)
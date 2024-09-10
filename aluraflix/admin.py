from django.contrib import admin
from aluraflix.models import Video

class Videos(admin.ModelAdmin):
    list_display = ('id','titulo','description','url',)
    list_display_links =('id','titulo',)
    list_per_page = 5
    search_fields = ('id','titulo')

admin.site.register(Video,Videos)
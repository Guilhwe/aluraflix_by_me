
from django.contrib import admin
from django.urls import path, include
from aluraflix.views import videos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/',videos)
]

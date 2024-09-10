
from django.contrib import admin
from django.urls import path, include
from aluraflix.views import VideoViewSet,VideoSerializer
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos',VideoViewSet,basename='videos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]

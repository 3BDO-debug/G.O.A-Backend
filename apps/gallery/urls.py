from django.urls import path
from . import handlers


urlpatterns = [path("gallery-images-data", handlers.gallery_images_handler)]

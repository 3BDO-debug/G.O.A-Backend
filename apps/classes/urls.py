from django.urls import path
from . import handlers


urlpatterns = [
    path("classes-data", handlers.classes_handlers),
    path("classes-descriptions-data", handlers.classes_descriptions_handler),
]

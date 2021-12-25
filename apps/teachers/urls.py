from django.urls import path
from . import handlers

urlpatterns = [path("teachers-data", handlers.teachers_handler)]

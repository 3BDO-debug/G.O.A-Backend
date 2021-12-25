from django.urls import path
from . import handlers

urlpatterns = [path("mail-data", handlers.mail_handler)]

from django.db import models

# Create your models here.
class Message(models.Model):
    full_name = models.CharField(max_length=350, verbose_name="Full name")
    phone_number = models.CharField(max_length=350, verbose_name="Phone number")
    message = models.TextField(verbose_name="Message")

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.full_name

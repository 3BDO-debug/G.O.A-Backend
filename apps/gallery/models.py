from django.db import models

# Create your models here.
class GalleryImage(models.Model):
    image_name = models.CharField(max_length=350, verbose_name="Image name")
    image = models.ImageField(upload_to="uploads/gallery_imgs", verbose_name="Image")

    class Meta:
        verbose_name = "Gallery image"
        verbose_name_plural = "Gallery images"

    def __str__(self):
        return self.image_name

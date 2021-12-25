from rest_framework.serializers import ModelSerializer
from . import models


class GalleryImageSerializer(ModelSerializer):
    class Meta:
        model = models.GalleryImage
        fields = "__all__"

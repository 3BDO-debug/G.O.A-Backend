from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


@api_view(["GET"])
def gallery_images_handler(request):
    gallery_images = models.GalleryImage.objects.all()
    gallery_images_serializer = serializers.GalleryImageSerializer(
        gallery_images, many=True
    )
    return Response(status=status.HTTP_200_OK, data=gallery_images_serializer.data)

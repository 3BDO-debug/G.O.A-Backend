from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


@api_view(["GET"])
def classes_handlers(request):
    classes = models.Class.objects.all()
    classes_serializer = serializers.ClassSerializer(classes, many=True)
    return Response(status=status.HTTP_200_OK, data=classes_serializer.data)


@api_view(["GET"])
def classes_descriptions_handler(request):
    class_descriptions = models.ClassDescription.objects.all()
    class_descriptions_serializer = serializers.ClassDescription(
        class_descriptions, many=True
    )
    return Response(data=class_descriptions_serializer.data, status=status.HTTP_200_OK)

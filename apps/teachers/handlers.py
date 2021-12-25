from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


@api_view(["GET"])
def teachers_handler(request):
    teachers = models.Teacher.objects.all()
    teachers_serializer = serializers.TeacherSerializer(teachers, many=True)
    return Response(status=status.HTTP_200_OK, data=teachers_serializer.data)

from rest_framework.serializers import ModelSerializer
from . import models


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = "__all__"

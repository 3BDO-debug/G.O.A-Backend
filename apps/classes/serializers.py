from rest_framework.serializers import ModelSerializer
from . import models


class ClassSerializer(ModelSerializer):
    class Meta:
        model = models.Class
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(ClassSerializer, self).to_representation(instance)
        representation["teacher_name"] = instance.teacher.teacher_name
        representation["teacher_photo"] = instance.teacher.teacher_photo.name
        return representation


class ClassDescription(ModelSerializer):
    class Meta:
        model = models.ClassDescription
        fields = "__all__"

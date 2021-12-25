from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models


@api_view(["POST"])
def mail_handler(request):
    models.Message.objects.create(
        full_name=request.POST.get("name"),
        phone_number=request.POST.get("phoneNumber"),
        message=request.POST.get("body"),
    ).save()
    return Response(status=status.HTTP_201_CREATED)

from django.shortcuts import render, HttpResponse
from USER import models


def test(request):
    models.UserType.objects.create(TypeName="growrterer", isDelete=False)
    return HttpResponse("1")

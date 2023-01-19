from django.shortcuts import render, HttpResponse
from USER import models


def test(request):
    models.UserType.objects.filter(TypeName="grower").delete()
    return HttpResponse("1")

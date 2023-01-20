from django.shortcuts import render, HttpResponse, redirect
from USER import models


def user_center(request, uid):
    user_type = request.session["info"].get("type", "")

    return HttpResponse("Welcome")

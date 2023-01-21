from django.shortcuts import render, HttpResponse, redirect
from USER import models


def user_center(request):
    user_type = request.session["info"].get("type", "")

    return render(request, "user_center_layout.html")

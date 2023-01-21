from django.shortcuts import render, HttpResponse, redirect
from USER.models import User
from USER.forms import UserProfileReadOnlyModelForm


def user_center(request):
    return render(request, "user_center_layout.html")


def user_profile(request):
    """
        Interface: user profile page
    """

    if request.method == "GET":
        user_object = User.objects.filter(uid=request.session["info"]["uid"]).first()
        form = UserProfileReadOnlyModelForm(instance=user_object)
        return render(request, "user_profile.html", {"form": form})

    """
       Business Logics: edit user profile
    """

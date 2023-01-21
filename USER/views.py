from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from USER.models import User
from USER.forms import UserProfileReadOnlyModelForm, PasswordForm


def user_center(request):
    return render(request, "user_center_layout.html")


@csrf_exempt
def user_profile(request):
    """
        Interface: user profile page
    """

    if request.method == "GET":
        user_object = User.objects.filter(uid=request.session["info"]["uid"]).first()
        profile_form = UserProfileReadOnlyModelForm(instance=user_object)
        password_form = PasswordForm()
        contex = {
            "profile_form": profile_form,
            "password_form": password_form,
        }
        return render(request, "user_profile.html", contex)


@csrf_exempt
def user_edit(request):
    """
       Business Logics: edit user profile
    """

    if request.method == "POST":
        user_object = User.objects.filter(uid=request.session["info"]["uid"]).first()
        form = UserProfileReadOnlyModelForm(data=request.POST, instance=user_object)
        if form.is_valid():
            form.save()
            data_dict = {"status": True, "url": "/user/profile/"}
            return JsonResponse(data_dict)

        data_dict = {"status": False, "errors": form.errors}
        return JsonResponse(data_dict)


@csrf_exempt
def user_password_change(request):
    """
       Business Logics: change user password
    """

    if request.method == "POST":
        password_form = PasswordForm(data=request.POST)
        user_object = User.objects.filter(uid=request.session["info"]["uid"]).first()

        if password_form.is_valid():

            # Check password

            if not check_password(password_form.cleaned_data["current_password"], user_object.password):
                password_form.add_error("current_password", "Please input correct password.")
                data_dict = {"status": False, "errors": password_form.errors}
                return JsonResponse(data_dict)

            User.objects.filter(uid=request.session["info"]["uid"]).update(
                password=password_form.cleaned_data["new_password"])
            data_dict = {"status": True, "url": "/user/profile/"}
            return JsonResponse(data_dict)

        data_dict = {"status": False, "errors": password_form.errors}
        return JsonResponse(data_dict)

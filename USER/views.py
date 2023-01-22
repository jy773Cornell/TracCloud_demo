from io import BytesIO
from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from USER.models import User, UserRelation
from USER.forms import UserLoginForm, UserCreateModelForm, UserProfileReadOnlyModelForm, PasswordChangeForm
from utils.ImgCaptcha import img_captcha


@csrf_exempt
def user_login(request):
    """
    Interface: login page and account creating page
    """

    if request.method == "GET":
        login_form = UserLoginForm()
        create_form = UserCreateModelForm()
        contex = {
            "login_form": login_form,
            "create_form": create_form,
        }
        return render(request, 'user_login&create.html', contex)


@csrf_exempt
def user_login_submit(request):
    """
    Business Logics: user login
    """

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():

            # Check captcha code

            user_input_code = form.cleaned_data.pop('code')
            code = request.session.get('image_code', "")
            if code.upper() != user_input_code.upper():
                form.add_error("code", "Validation error!")
                data_dict = {"status": False, "errors": form.errors}
                return JsonResponse(data_dict)

            # Check username and password

            user_object = User.objects.filter(
                username=form.cleaned_data["username"],
                self_activated=True,
                is_active=True,
            ).first()

            if not user_object:
                form.add_error("username", "Input username doesn't exist.")
                data_dict = {"status": False, "errors": form.errors}
                return JsonResponse(data_dict)

            uid = user_object.uid
            username = user_object.username
            type_name = user_object.type.type_name
            password = user_object.password

            if not check_password(form.cleaned_data["password"], password):
                form.add_error("password", "Please enter the correct password.")
                data_dict = {"status": False, "errors": form.errors}
                return JsonResponse(data_dict)

            # Successful login, the web will generate a cookie and write user info into session.

            request.session["info"] = {"uid": uid, "username": username, "type": type_name}
            request.session.set_expiry(60 * 60 * 24)

            # Check whether the user is an admin, if so, login and redirect to '/admin/'

            if type_name == "admin":
                admin_user = authenticate(username=username, password=form.cleaned_data["password"])
                if admin_user is not None:
                    login(request, admin_user)
                data_dict = {"status": True, "url": "/admin/"}
                return JsonResponse(data_dict)

            # General user will go to '/user/center/'

            data_dict = {"status": True, "url": "/user/center/"}
            return JsonResponse(data_dict)

        data_dict = {"status": False, "errors": form.errors}
        return JsonResponse(data_dict)


def user_logout(request):
    if request.method == "GET":
        request.session.clear()
        return redirect("/login/")


@csrf_exempt
def user_create(request):
    """
    Business Logics: account creation
    """

    if request.method == "POST":
        form = UserCreateModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            data_dict = {"status": True, "url": "/user/login/"}
            return JsonResponse(data_dict)

        data_dict = {"status": False, "errors": form.errors}
        return JsonResponse(data_dict)


@csrf_exempt
def user_delete(request):
    """
       Business Logics: delete user account
    """

    if request.method == "POST":
        uid = request.session["info"]["uid"]

        related_user = UserRelation.objects.filter(Q(requester_id=uid) | Q(provider_id=uid))
        if related_user:
            data_dict = {"status": False, "errors": "This account is being connected with other users."}
            return JsonResponse(data_dict)

        User.objects.filter(uid=uid).delete()
        data_dict = {"status": True, "url": "/user/login/"}
        return JsonResponse(data_dict)


def user_center(request):
    """
       Interface: user center page
   """

    if request.method == "GET":
        return render(request, "user_center.html")


@csrf_exempt
def user_profile(request):
    """
        Interface: user profile page
    """

    if request.method == "GET":
        user_object = User.objects.filter(uid=request.session["info"]["uid"]).first()
        profile_form = UserProfileReadOnlyModelForm(instance=user_object)
        password_form = PasswordChangeForm()
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
        password_form = PasswordChangeForm(data=request.POST)
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


def image_code(request):
    img, code_string = img_captcha()

    request.session["image_code"] = code_string
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')

    return HttpResponse(stream.getvalue())

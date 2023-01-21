from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from USER.models import User


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info in ["/login/", "/login/submit/", "/account/create/", "/image/code/", ]:
            return

        info_dict = request.session.get("info")
        if info_dict:
            if check_user_status(request):
                return

        return redirect("/login/")

    def process_response(self, request, response):
        return response


def check_user_status(request):
    user_object = User.objects.filter(
        uid=request.session["info"]["uid"],
        self_activated=True,
        is_active=True,
    ).first()

    if user_object:
        return True

    return False

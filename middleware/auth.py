import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):

        if re.match("/admin/", request.path_info):
            return

        info_dict = request.session.get("info")
        if info_dict:
            if request.path_info == "/login/":
                return HttpResponse("Login successfully")
            return

        if request.path_info in ["/login/", "/image/code/"]:
            return

        return redirect("/login/")

    def process_response(self, request, response):

        return response

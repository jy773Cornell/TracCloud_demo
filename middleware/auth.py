import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect, HttpResponse


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info in ["/login/", "/image/code/", "/create/account/"]:
            return

        info_dict = request.session.get("info")
        if info_dict:
            return

        return redirect("/login/")

    def process_response(self, request, response):

        return response

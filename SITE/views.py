from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from USER.models import User, UserRelation
from SITE.forms import TopSiteModelForm


def site_list(request):
    top_site_form = TopSiteModelForm()
    context = {
        "top_site_form": top_site_form,
    }
    return render(request, "site_list.html", context)

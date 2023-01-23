from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from SITE.models import SiteType
from SITE.forms import TopSiteModelForm, MiddleSiteModelForm, BaseSiteModelForm


def site_list(request):
    """
       Interface: login page and account creating page
    """

    if request.method == "GET":
        top_site_form = TopSiteModelForm()
        mid_site_form = MiddleSiteModelForm()
        context = {
            "top_site_form": top_site_form,
            "mid_site_form": mid_site_form,
        }
        return render(request, "site_list.html", context)


@csrf_exempt
def site_top_type_change(request):
    if request.method == "POST":
        top_site = request.POST["top_site"]
        parent_stid = SiteType.objects.filter(name=top_site, is_active=True).first().stid
        mid_site_objects = SiteType.objects.filter(parent_type_id=parent_stid, is_active=True)
        site_list = []
        for mid_site in mid_site_objects:
            site_list.append(mid_site.name)

        data_dict = {"status": True, "data": site_list}
        return JsonResponse(data_dict)

"""TracCloud_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
import USER.views as user
import ACCOUNT.views as account

urlpatterns = [
    # Media files

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    # Admin center

    path('admin/', admin.site.urls),

    # Account login & logout & account creation

    path('login/', account.user_login),
    path('logout/', account.user_logout),
    path('create/account/', account.user_create),
    path('image/code/', account.image_code),

    # User center

    path('user/center/<str:uid>/', user.user_center),

]

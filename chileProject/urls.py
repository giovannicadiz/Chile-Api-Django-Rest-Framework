"""chileProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from chileApp.views import RegionList, RegionDetail, ProvinciaList, ProvinciaDetail, ComunaList, ComunaDetail


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^regiones/$', RegionList.as_view()),
    url(r'^regiones/(?P<pk>[0-9]+)/$', RegionDetail.as_view()),

    url(r'^provincias/$', ProvinciaList.as_view()),
    url(r'^provincias/(?P<pk>[0-9]+)/$', ProvinciaDetail.as_view()),

    url(r'^comunas/$', ComunaList.as_view()),
    url(r'^comunas/(?P<pk>[0-9]+)/$', ComunaDetail.as_view()),
]


















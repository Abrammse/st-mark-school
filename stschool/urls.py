"""
URL configuration for stschool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import  path
from stschool import views
from django.conf import settings
from django.conf.urls.static import  static




urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index,name="home"),
    path("new", views.new, name="new"),
    path("al7an1/",views.al7an1,name="al7an1"),
    path("al7an11/", views.al7an11, name="al7an11"),
    path("al7an12/", views.al7an12, name="al7an12"),
    path("al7an13/", views.al7an13, name="al7an13"),

    path("al7an2/",views.al7an2,name="al7an2"),
    path("al7an21/", views.al7an21, name="al7an21"),
    path("al7an22/", views.al7an22, name="al7an22"),
    path("al7an23/", views.al7an23, name="al7an23"),

    path("al7an3/",views.al7an3,name="al7an3"),
    path("al7an31/", views.al7an31, name="al7an31"),
    path("al7an32/", views.al7an32, name="al7an32"),
    path("al7an33/", views.al7an33, name="al7an32"),

    path("Agpia1/", views.Agpia1, name="Agpia1"),
    path("Agpia11/", views.Agpia11, name="Agpia11"),
    path("Agpia12/", views.Agpia12, name="Agpia12"),
    path("Agpia13/", views.Agpia13, name="Agpia13"),

    path("Agpia2/", views.Agpia2, name="Agpia2"),
    path("Agpia21/", views.Agpia21, name="Agpia21"),
    path("Agpia22/", views.Agpia22, name="Agpia22"),
    path("Agpia23/", views.Agpia23, name="Agpia23"),

    path("Agpia3/", views.Agpia3, name="Agpia3"),
    path("Agpia31/", views.Agpia31, name="Agpia31"),
    path("Agpia32/", views.Agpia32, name="Agpia32"),
    path("Agpia33/", views.Agpia33, name="Agpia33"),

    path("kpaty1/", views.kpaty1, name="kpaty1"),
    path("kpaty11/", views.kpaty11, name="kpaty11"),
    path("kpaty12/", views.kpaty12, name="kpaty12"),
    path("kpaty13/", views.kpaty13, name="kpaty13"),

    path("kpaty2/", views.kpaty2, name="kpaty2"),
    path("kpaty21/", views.kpaty21, name="kpaty21"),
    path("kpaty22/", views.kpaty22, name="kpaty22"),
    path("kpaty23/", views.kpaty23, name="kpaty23"),

    path("kpaty3/", views.kpaty3, name="kpaty3"),
    path("kpaty31/", views.kpaty31, name="kpaty31"),
    path("kpaty32/", views.kpaty32, name="kpaty32"),
    path("kpaty33/", views.kpaty33, name="kpaty33"),

    path("taks1/", views.taks1, name="taks1"),
    path("taks11/", views.taks11, name="taks11"),
    path("taks12/", views.taks12, name="taks12"),
    path("taks13/", views.taks13, name="taks13"),

    path("taks2/", views.taks2, name="taks2"),
    path("taks21/", views.taks21, name="taks21"),
    path("taks22/", views.taks22, name="taks22"),
    path("taks23/", views.taks23, name="taks23"),

    path("taks3/", views.taks3, name="taks3"),
    path("taks31/", views.taks31, name="taks31"),
    path("taks32/", views.taks32, name="taks32"),
    path("taks33/", views.taks33, name="taks33"),
    path("photo/", views.Abram,name="photo"),
    path("newac/", views.send,name="newac"),
    path("system/", views.system, name="system"),
    path("login/", views.login_view, name="login"),
    path("search/", views.search_school, name="search"),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
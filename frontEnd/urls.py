from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage # for /favicon.ico
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contentPages/aboutMe.html", views.aboutMe, name="aboutMe"),
    path("contentPages/coding.html", views.coding, name="coding"),
    path("contentPages/research.html", views.research, name="research"),
    path("contentPages/publications.html", views.publications, name="publications"),
    path("contentPages/contact.html", views.contact, name="contact"),
    path("contentPages/comingSoon.html", views.comingSoon, name="comingSoon"),
    path("contentPages/<path:other_path>", views.nonexistentSubpage, name="nonexistentSubpage"),


    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('frontEnd/icons/favicon.ico'))),
    path("<path:other_path>", views.nonexistent, name="nonexistent"),
]
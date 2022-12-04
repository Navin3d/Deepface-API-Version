from django.urls import path
from . import views


urlpatterns = [
    path("find/", views.find),
    path("analize/", views.analize),
    path("verify/", views.verify),
]

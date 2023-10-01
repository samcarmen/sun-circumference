from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path(
        "sun_circumference/",
        views.sun_circumference,
        name="sun_circumference",
    ),
]

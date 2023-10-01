from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html")


@api_view(["GET"])
def sun_circumference(request):
    # Fetch the latest value of π from the cache
    latest_pi = cache.get("pi_value")

    if latest_pi is None:
        return Response({"error": "Value of Pi not computed yet!"}, status=404)

    sun_radius = 696340  # in kilometers
    circumference = 2 * float(latest_pi) * sun_radius

    data = {
        "pi_value": latest_pi,
        "circumference": f"{circumference} kilometers",
    }

    return Response(data)

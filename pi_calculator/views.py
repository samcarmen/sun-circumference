from decimal import Decimal

from django.core.cache import cache
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


def homepage(request):
    return render(request, "homepage.html")


@api_view(["GET"])
def sun_circumference(request):
    # Fetch the latest value of π from redis cache
    latest_pi = cache.get("pi_value")

    if latest_pi is None:
        return Response({"error": "Value of Pi not computed yet!"}, status=404)

    sun_radius = 696340
    circumference = 2 * Decimal(latest_pi) * sun_radius

    data = {
        "pi_value": str(latest_pi),
        "circumference": f"{str(circumference)} kilometers",
    }

    return Response(data)

import math
from decimal import Decimal, getcontext
from time import sleep

from celery import shared_task
from django.core.cache import cache


def compute_pi_chudnovsky(precision):
    getcontext().prec = precision + 2  # extra digits for intermediate steps
    C = 426880 * math.sqrt(10005)
    K = Decimal(6)
    M = Decimal(1)
    X = Decimal(1)
    L = Decimal(13591409)
    Ks = Decimal(545140134)
    S = L

    for i in range(1, precision):
        M = K * (K * K - 16) * M / i**3
        L += Ks
        X *= -262537412640768000
        S += Decimal(M * L) / X

    pi = Decimal(C) / S
    getcontext().prec = precision  # set back to desired precision
    return +pi  # unary plus rounds to desired precision


@shared_task
def compute_pi_indefinitely():
    precision = 1
    while True:
        pi_value = compute_pi_chudnovsky(precision)
        # Store pi_value in Redis
        cache.set("pi_value", pi_value)

        precision += 1
        # Add a delay to prevent extremely rapid calculations
        sleep(2)

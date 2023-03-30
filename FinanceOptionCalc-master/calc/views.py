from django.shortcuts import render
from django.http import HttpResponse

import numpy as np
import scipy.stats as ss


# -----------------------------European calculation using Black-Scholes-----------------------------------------
def d1(S0, sigma, r, T, K):
    return (np.log(S0 / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))


def d2(S0, sigma, r, T, K):
    return (np.log(S0 / K) + (r - sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))


def get_european(S0, sigma, r, T, K, option_type):
    if option_type == "C":
        return round(S0 * ss.norm.cdf(d1(S0, sigma, r, T, K)) - K * np.exp(-r * T) * ss.norm.cdf(d2(S0, sigma, r, T, K)), 4)
    else:
        return round(K * np.exp(-r * T) * ss.norm.cdf(-d2(S0, sigma, r, T, K)) - S0 * ss.norm.cdf(-d1(S0, sigma, r, T, K)), 4)


# --------------------------------------------------------------------------
def index(request):
    return render(request, 'index.html')


def european(request, S, sigma, r, T, K, call_put):
    c = get_european(int(S), float(sigma), float(r), float(T), float(K), str(call_put))
    r = HttpResponse(str(c))
    return r

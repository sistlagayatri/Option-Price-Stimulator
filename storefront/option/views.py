from django.shortcuts import render
from django.http import HttpResponse

import math
import numpy as np

def facto(n,i):
    return math.factorial(n)/(math.factorial(n-i)*math.factorial(i))

def binomial(S0, K , T, r, u,d, N, opt = 'call'):
    p= (np.exp(r*T/N)-d)/(u-d)
    price1=0
    for i in range(N+1):
        s1= S0*(u**i)*(d**(N-i))
        p1=facto(N,i)*(p**i)*((1-p)**(N-i))
        if opt== 'call':
            price1=price1+max(s1-K,0)*p1
        elif opt=='put':
            price1+=max(K-s1,0)*p1
        else:
            print("Please type only put or call in opt textfield")
    return np.exp(-r*T)*price1



def binomialcalc(request):
    S0=int(request.GET["S0"])
    K=float(request.GET["K"])
    T=float(request.GET["T"])
    r=float(request.GET["r"])
    u=float(request.GET["u"])
    d=float(request.GET["d"])
    N=int(request.GET["N"])
    opt=request.GET["opt"]
    res= binomial(S0,K,T,r,u,d,N,opt)
    return render(request,'option/result.html',{"result":res})


def index(request):
    return render(request,'option/index.html')

def index1(request):
    return render(request,'option/european.html')

def index2(request):
    return render(request,'option/europeanblack.html')


from scipy.stats import norm

N = norm.cdf

def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r*T)* N(d2)

def BS_PUT(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*N(-d1)

def res2(opt,S, K, T, r, sigma):
    if opt == 'call' :
        return BS_CALL(S, K, T, r, sigma)
    elif opt == 'put':
        return BS_PUT(S, K, T, r, sigma)
    else:
            print("Please type only put or call in opt textfield")


def black(request):
    S=float(request.GET["S"])
    K=float(request.GET["K"])
    T=float(request.GET["T"])
    r=float(request.GET["r"])
    sigma=float(request.GET["sigma"])
    opt=request.GET["opt"]
    resu= res2(opt,S, K, T, r, sigma)
    return render(request,'option/result1.html',{"result1":resu})

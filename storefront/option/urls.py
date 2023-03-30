from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('add1', views.index1, name='add1'),
    path('black1', views.index2, name='black1'),
     path('add', views.binomialcalc, name='add'),
    path('black', views.black, name='black')
]
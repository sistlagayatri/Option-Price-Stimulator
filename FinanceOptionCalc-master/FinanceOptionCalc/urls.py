from django.urls import include, re_path

from django.contrib import admin
from calc.views import european, index
admin.autodiscover()


urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^european_index', index, name='index'),
    re_path(r'^european/S(.+)sigma(.+)r(.+)T(.+)K(.+)call_put(.+)/$', european, name='european'),
]

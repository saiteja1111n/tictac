__author__ = 'RADHAKRISHNA'

from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^login/$',login),
    url(r'^startgame/$',startgame),
    url(r'^register/$',register),
    url(r'^userregister/$',registerform),
    url(r'^$', loginform),
    url(r'^nextstep/',checkstatus),
]


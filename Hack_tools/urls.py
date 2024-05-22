from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path("scanning",views.scanning,name="ScanningPage"),
    path("firewall",views.firewall,name="FirewallPage"),
    path("ping",views.ping,name="PingPage"),
]
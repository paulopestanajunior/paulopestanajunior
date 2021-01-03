"""nyctaxi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import  url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from taxi import views

router = routers.DefaultRouter()
router.register(r'taxis', views.TaxiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^getDatabase/', views.getDatabase.as_view()),
    path('taxi/', views.TaxiAPIView.as_view()),
    path('dash/', views.dashboard_home, name="dashboard"),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
"""stocks_viz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

#pour lié l'url à la vu
from myStocks.views import stocks
from myStocks.views import home

urlpatterns = [
    
    path("", home),
    path("ndays=<int:ndays>&&ncurrencies=<str:ncurrencies>", stocks), #page d'accueil mon url doit etre sous cette forme
    #2 param qui doivent etre les memes que ceux de la views si non erreur car c'est eu qui serront envoyé à la vu
    path('admin/', admin.site.urls),
]

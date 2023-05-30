"""inazuma_rest URL Configuration

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
from InazumaApp.endpoints import players, objects, clubs, seasons
# oid = object id || pid = players id || cid = club id || sid = seasons id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players', players.playersSearch),
    path('players/', players.playersSearch),
    path('objects', objects.objectsSearch),
    path('objects/<int:oid>', objects.objectById),
    path('players/<int:pid>', players.playersByID),
    path('clubs/<int:cid>', clubs.clubsByID),
    path('seasons/<int:sid>', seasons.seasonsByID)
]

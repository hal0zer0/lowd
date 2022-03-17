"""lowd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from lowdcore import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(views.HomeView.as_view()), name="home"),
    path('check_new/', views.check_new, name="check_new"),
    path('new_player/', login_required(views.NewPlayerView.as_view()), name="new_player"),
    path('town_square/', login_required(views.TownSquareView.as_view()), name="town_square"),
    path('forest/', login_required(views.ForestView.as_view()), name="forest"),
    path('forest/look', login_required(views.FightView.as_view()), name="fight"),
    path('weapons/', login_required(views.WeaponShopView.as_view()), name="weapon_shop"),
    path('bank/', include('lowdbank.urls')),
]

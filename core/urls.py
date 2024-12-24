"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from musicapp import views
from core import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

handler404 = 'musicapp.views.tr_handler404'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path('playlist/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
    path("login/", views.LoginUser.as_view(), name="login"),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path("logout/", views.logout_view, name='logout'),
    path("profile/", views.ProfileUser.as_view(), name='profile'),
    path('player/', include("musicapp.urls")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

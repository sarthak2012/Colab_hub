from django.contrib import admin
from django.urls import path
from collab import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("home", views.home, name='home'),
    path("download", views.download, name='download'),
]
from django.contrib import admin
from django.urls import path
from collab import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.login, name='home'),
    path("index", views.index, name='index'),
    path("todo", views.todo, name='todo'),
    path("chatting", views.chatting, name='chatting'),
    path("sharing", views.sharing, name='sharing'),
    path('upload/', views.upload_file, name='upload_file'),
    path("meeting",views.videocall, name='meeting'),
    path('signup/', views.save_login_data, name='signup'),
    path('save_login_data/', views.save_login_data, name='save_login_data'),
]
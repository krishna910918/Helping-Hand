from django.urls import path, re_path
from .  import views

urlpatterns = [
    path('',views.chatAll),
    re_path(r'^(?P<un>\w+)/$', views.chat), 
]

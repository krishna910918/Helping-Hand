from django.urls import path, re_path
from .  import views

urlpatterns = [
    path('',views.chat),
    re_path(r'^(?P<un>\w+)/$', views.chat), #TODO: catch username from url
]

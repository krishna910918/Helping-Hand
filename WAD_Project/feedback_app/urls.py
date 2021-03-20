from django.urls import path
from .  import views

urlpatterns = [
     path('',views.feedback,name = 'feedback'),
    path('accept_feedback', views.accept_form, name = 'accept_feedback'),
]

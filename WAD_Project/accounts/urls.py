from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('signup',views.signup,name = 'signup'),
    path('signin',views.signin,name = 'signin'),
    path('signout',views.signout,name = 'signout'),
    path('signinviadon',views.signinviadon,name = 'signinviadon'),
    path('signinviarec',views.signinviarec,name = 'signinviarec'),
    
]
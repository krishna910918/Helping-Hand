from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

  
urlpatterns = [
    path ('', views.homepage,name = 'homepage'),
    path ('contactus/', views.contactus,name = 'contactus'),
    path ('aboutus/', views.aboutus,name = 'aboutus'),
    path ('information/', views.information,name = 'information'),
    path ('donation/', views.donation,name = 'donation'),
    path ('receive/', views.receive,name = 'receive'),
    path('history/',views.history,name='history'),
    
    ]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
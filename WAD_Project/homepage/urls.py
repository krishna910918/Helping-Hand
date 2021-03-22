from django.urls import path
from .views import homepage, contactus, aboutus, information, donation, receive

  
urlpatterns = [
    path ('', homepage),
    path ('contactus/', contactus),
    path ('aboutus/', aboutus),
    path ('information/', information),
    path ('donation/', donation),
    path ('receive/', receive),
]
from django.contrib import admin
from .models import Donation,Receive,Collected

# Register your models here.

admin.site.register(Donation)
admin.site.register(Receive)
admin.site.register(Collected)


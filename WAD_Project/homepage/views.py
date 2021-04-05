from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Donation

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def donation(request):
    context={
        'status_display':'none',
        'form_display':'block',
    }
    if request.method == 'POST':
        print(request.POST)
        district = request.POST['district']
        category = request.POST['category']
        image = request.FILES['image']
        description = request.POST['description']
        contact = request.POST['contact']

        donation = Donation()

        donation.district=district
        donation.category=category
        donation.img=image
        donation.desc=description
        donation.cont=contact
        donation.save()

        context={
            'status_display':'block',
            'form_display':'none',
        }
    elif request.user.is_authenticated :
        return render(request, 'donation.html',context)
    else :
        
        return redirect('signinviadon')

def receive(request):
    if request.user.is_authenticated:
        return render(request, 'receive.html')
    else :
        return redirect('signinviarec')

def information(request):
    return render(request, 'information.html')


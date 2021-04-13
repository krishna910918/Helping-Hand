from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Donation,Receive

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def donation(request):
    if not request.user.is_authenticated :
        return redirect('signinviadon')
    context={
            'status_display':'none',
            'form_display':'block',
            }
    if request.method == "POST":
            donation = Donation()
            donation.username=request.user.username
            donation.name=request.user.first_name
            donation.country=request.POST['country']
            donation.state=request.POST['state']
            donation.district=request.POST['district']
            donation.category=request.POST['category']
            donation.img=request.FILES['image']
            donation.desc=request.POST['description']
            donation.cont=request.POST['contact']
            donation.save()

            context={
                'status_display':'block',
                'form_display':'none',
            }
    return render(request, 'donation.html',context)
        
    
   
def receive(request):
    if not request.user.is_authenticated:
        return redirect('signinviarec')
    if request.method == "POST":
        receive = Receive() 
        receive.username = request.user.username
        receive.name = request.user.first_name 
        receive.country = request.POST['country']
        receive.state = request.POST['state']
        receive.district = request.POST['district']
        receive.category = request.POST['category']

        request_obj = Donation.objects.filter(state=request.POST['state'] , district = request.POST['district'], category = request.POST['category'])
        return render(request, 'receive_filter.html',{'request_obj':request_obj})
    return render(request, 'receive.html')


def history(request):
    donation_obj = Donation.objects.filter(username = request.user.username,name = request.user.first_name)
    receive_obj = Receive.objects.filter(username = request.user.username,name = request.user.first_name)
    return render(request, 'history.html',{'donation_obj':donation_obj ,'receive_obj':receive_obj,})

def information(request):
    return render(request, 'information.html')


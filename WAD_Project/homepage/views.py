from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Donation,Receive,Collected 
import datetime

# Create your views here.
# Function for Homepage
def homepage(request):
    is_there_obj=False 
    claimed_obj = None
    # to find whether claimed item is collected or not.
    if request.method == "POST":
        obj = Receive.objects.filter(id=request.POST['ID'])[0]
        obj.collected = True  # item collected
        collected=Collected() 
        collected.username = request.user.username  
        collected.name = request.user.first_name 
        collected.country = obj.country
        collected.state = obj.state
        collected.district = obj.district
        collected.category = obj.category
        collected.img = obj.img
        collected.desc = obj.desc
        collected.cont = obj.cont
        collected.donor_name = obj.donor_name
        collected.save() #saving Collected object to database.
        obj.save() #updating collected=True in database for Receive model.

    # To show a modal(pop-up box) if item is not collected.
    try:
        claimed_obj = Receive.objects.filter(collected=False ,username = request.user.username,name = request.user.first_name)
        count=Receive.objects.filter(collected=False ,username = request.user.username,name = request.user.first_name).count()
        if count>0:
            is_there_obj = True
    except:
        pass
    return render(request, 'homepage.html',{'claimed_obj':claimed_obj,'is_there_obj':is_there_obj})

#Function for Aboutus Page
def aboutus(request):
    return render(request, 'aboutus.html')

#Function for ContactUs page
def contactus(request):
    return render(request, 'contactus.html')

#Function for Donation page
def donation(request):
    #User cannot enter into Donation Page without completion of Authentication.
    if not request.user.is_authenticated :
        return redirect('signinviadon')

    #to show form to fill and upload
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
            donation.save() #saving the donated item in Donation model. 

            #To show message(Uploaded) after saving into database.
            context={
                'status_display':'block',
                'form_display':'none',
            }
    return render(request, 'donation.html',context)
        
    
# Function for Receive Page  
def receive(request):
    #User cannot enter into receive Page without completion of Authentication
    if not request.user.is_authenticated:
        return redirect('signinviarec')
    try:
        claim_obj = Donation.objects.filter(id=request.POST['ID'])
        claim_obj = claim_obj[0]
        
        receive=Receive()
        receive.username = request.user.username
        receive.name = request.user.first_name 
        receive.country = claim_obj.country
        receive.state = claim_obj.state
        receive.district = claim_obj.district
        receive.category = claim_obj.category
        receive.img = claim_obj.img
        receive.desc = claim_obj.desc
        receive.cont = claim_obj.cont
        receive.donor_name = claim_obj.username
        all_received_obj = Receive.objects.filter(username=request.user.username)
        all_received_obj_count = Receive.objects.filter(username=request.user.username).count()
        if all_received_obj_count > 0: #To make limit for claiming.
            for obj in all_received_obj:
                received_date_time = obj.created
                received_date = str(received_date_time).split(' ')[0]
                current_date = str(datetime.datetime.now()).split(' ')[0]
                if received_date == current_date:
                    #Per day an User can claim only one object.
                    return render(request, 'receive.html',{'limits_exceeded':'True'}) #If limit is exceeded ,they redirected to Receive page with a warning.
                print(received_date,datetime.datetime.now())

        claim_obj.claimed=True
        receive.save() #save in database for Receive model.
        claim_obj.save() #Updation in Database as claimed.
        return redirect('/chat/' + str(receive.donor_name) + '/') #redirect to chat with donor.
    except:
        pass
    if request.method == "POST":
        display_state_wise = 'none'
        display_msg = 'none'
        r1_obj = Donation.objects.filter(claimed = False,state=request.POST['state'] , district = request.POST['district'], category = request.POST['category'])
        r1_obj_count = Donation.objects.filter(claimed = False,state=request.POST['state'] , district = request.POST['district'], category = request.POST['category']).count()
        if not r1_obj_count>0: #If no objects are available in choosen district ,the objects will filtered through state.
            display_state_wise = 'block'
            r1_obj = Donation.objects.filter(claimed = False,state=request.POST['state'] , category = request.POST['category'])
            r1_obj_count = Donation.objects.filter(claimed = False,state=request.POST['state'] , category = request.POST['category']).count()
            if not r1_obj_count>0: #If no objects are available in State , message will be shown. 
                display_msg = 'block'
                display_state_wise = 'none'
        r2_obj = Donation.objects.exclude(username = request.user.username) #A Donor restricted to claim which was donated by himself.
        request_obj = r1_obj & r2_obj

        return render(request, 'receive_filter.html',{'request_obj':request_obj , 'display_state_wise':display_state_wise ,'display_msg':display_msg}) #A Objects list page where receiver can claim.
    return render(request, 'receive.html')


#Function for History Page.
def history(request):
    donation_obj = Donation.objects.filter(username = request.user.username,name = request.user.first_name) #Objects donated by User.
    collected_obj = Receive.objects.filter(collected=True ,username = request.user.username,name = request.user.first_name) #Objects collected by user.
    claimed_obj = Receive.objects.filter(collected=False ,username = request.user.username,name = request.user.first_name)#Objects claimed but not collected.
    return render(request, 'history.html',{'donation_obj':donation_obj ,'collected_obj':collected_obj,'claimed_obj':claimed_obj})

#Function for Request Page.
def information(request):
    return render(request, 'information.html')


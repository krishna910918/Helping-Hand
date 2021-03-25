from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def donation(request):
    return render(request, 'donation.html')

def receive(request):
    return render(request, 'receive.html')

def information(request):
    return render(request, 'information.html')

def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')
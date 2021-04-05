from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

def signup(request):

    if request.method == 'POST' :
        u = request.POST['u'];
        f = request.POST['f'];
        l = request.POST['l'];
        e = request.POST['e'];
        p1 = request.POST['p1'];
        p2 = request.POST['p2'];
        c = request.POST['c'];

        if p1 == p2 :
            if User.objects.filter(username=u).exists():
                messages.info(request,'User name already taken')
                return redirect('signup')
            elif User.objects.filter(email=e).exists():
                messages.info(request,'Email ID already taken')
                return redirect('signup')
            else :
                if len(p1) == 0 or len(p2) == 0 or len(u) == 0 or len(f) == 0 or len(l) == 0 or len(e) == 0 :
                    messages.info(request,'Please fill all the credentials')
                    return redirect('signup');

                else :
                    user = User.objects.create_user(username = u,password = p1,email = e,first_name = f,last_name = l);
                    user.save();
                    messages.info(request,'Your account is been created successfully,Now login to the website');
                    return redirect('signin')
        else :
            messages.info(request,'password not matching...');
            return redirect('signup')
        return redirect('/')
        

    else :

         return render(request,'signup.html');

def signin(request):
    if request.method == 'POST' :
        u = request.POST['u'];
        p = request.POST['p'];

        user = auth.authenticate(username=u,password=p)
        if user is not None :
            auth.login(request,user);
            return redirect('/')
        else :
            messages.info(request,'Invalid username or password or both')
            return redirect('signin');

    else : 
        return render(request,'signin.html');

def signout(request):
    auth.logout(request);
    return redirect('/');

def signinviadon(request):
    if request.method == 'POST' :
        u = request.POST['u'];
        p = request.POST['p'];

        user = auth.authenticate(username=u,password=p)
        if user is not None :
            auth.login(request,user);
            return redirect('donation')
        else :
            messages.info(request,'Invalid username or password or both')
            return redirect('signinviadon');

    else : 
        return render(request,'signinviadon.html');

def signinviarec(request):
    if request.method == 'POST' :
        u = request.POST['u'];
        p = request.POST['p'];

        user = auth.authenticate(username=u,password=p)
        if user is not None :
            auth.login(request,user);
            return redirect('receive')
        else :
            messages.info(request,'Invalid username or password or both')
            return redirect('signinviarec');

    else : 
        return render(request,'signinviarec.html');



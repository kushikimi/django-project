from django.shortcuts import render
from .forms import user_form
from .forms import user_profile_form
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def Reg(request):
    registered=False
    if request.method=='POST':
        my_form=user_form(request.POST)
        profile_form=user_profile_form(request.POST)
        if my_form.is_valid() and profile_form.is_valid():
            myuser=my_form.save()
            myuser.set_password(myuser.password)
            myuser.save()
            prof=profile_form.save(commit=False)
            prof.user=myuser
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                prof.profile_pic = request.FILES['profile_pic']

            # Now save model
            prof.save()
            registered=True
        else:
            print("error")
    else:
        my_form=user_form()
        profile_form=user_profile_form()
    return render(request,'register.html',{'my_form':my_form,'profile_form':profile_form,'registered':registered})




def user_login(request):
    if request.method=="POST":
        musername=request.POST.get("fusername")
        mpassword=request.POST.get("fpassword")
        user_auth=authenticate(username=musername,password=mpassword)
        if user_auth:
            print('authenticated')
            login(request,user_auth)
            return HttpResponse('welcome')
        else:
            return HttpResponse('invalid user')
    else:
        return render(request,'login.html',{})


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('app:user_login'))



@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# def login(request):
    
def login_(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        u = authenticate(username = username,
                         password = password)
        if u:
            login(request,u)
            return redirect('home')
        else:
            return render(request,'login_.html',{'error':'username or password is wrong...!'})
    return render(request,'login_.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        username = request.POST['uname']
        password = request.POST['password']
        try:
            u = User.objects.get(username = username)
            return render(request,'register.html',{'error':'username is already taken'})
        except:
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
        return redirect('login_')
    return render(request,'register.html')

def forgotpass(request):
    return render(request,'forgotpass.html')

@login_required(login_url='login_')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='login_')
def logout_(request):
    logout(request)
    return redirect('login_')

@login_required
def edit_profile(request):

    user = request.user

    if request.method == "POST":
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.email = request.POST.get('email')
        user.username = request.POST.get('uname')

        user.save()

        return redirect('profile')

    return render(request, 'edit.html')
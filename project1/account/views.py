from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages,auth

# Create your views here.


# def register(request):
#  return render(request,'register.html')
# def logout(request):
#  return render(request,'logout.html')
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            # Successful login, you can redirect to a dashboard or profile page
            return redirect('user_login')  
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('user_login')  # Redirect back to the login page
    else:
     return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email=request.POST['email']
        name=request.POST['name']
        password=request.POST['password']
        username=request.POST['username']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already registerd')
                return redirect('user_login')
            else:
                user=User.objects.create_user(username=username,first_name=name,email=email,password=password)
                user.save()
                messages.info(request,'User created')
                return redirect('user_login')
        else:
             messages.error(request,'Password doesnot matched')
             return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
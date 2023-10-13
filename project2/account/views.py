from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages,auth
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage

# Create your views here.
# def user_login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(request,username=username,password=password)# kbkbk zbzx

#         if user is not None:
#             login(request,user)
#             messages.info(request,'Login successful')
#             return redirect('home')
#         else:
#             messages.error(request,'Username or Password is not matching')
#             return redirect('user_login')
#     else:
#         return render(request,'login.html')
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)# kbkbk zbzx

        if user is not None:
            login(request,user)
            #messages.info(request,"Login successful")
            return redirect('home')
        else:
            messages.error(request,"Username or Password is not matching")
            return redirect('user_login')
    else:
        return render(request,'login.html')

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')  # Use get() to avoid KeyError
#         password = request.POST.get('password')

#         # Authenticate user
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Login successful')  # Using success() instead of info()
#             return redirect('home')  # Make sure you have a URL pattern named 'home'
#         else:
#             messages.error(request, 'Invalid username or password')  # General error message
#             return redirect('user_login')
#     else:
#         return render(request, 'login.html')
# def register(request):
#     if request.method == 'POST':
#         email=request.POST['email']
#         first_name=request.POST['name']
#         password=request.POST['password']
#         username=request.POST['username']
#         cpassword=request.POST['cpassword']
#         if password==cpassword:
#             if User.objects.filter(email=email).exists():
#                 messages.error(request,'Email already registerd')
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
#                 user.save()
#                 messages.info(request,'User created')

#     else:
#         return render(request,'register.html')

# def register(request):
#     if request.method == 'POST':
#         email=request.POST['email']
#         first_name=request.POST['name']
#         password=request.POST['password']
#         username=request.POST['username']
#         cpassword=request.POST['cpassword']
#         if password==cpassword:
#             if User.objects.filter(email=email).exists():
#                 messages.error(request,'Email already registerd')
#                 return redirect('user_login')
#             else:
#                 user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
#                 user.save()
#                 messages.info(request,'User created')
#                 return redirect('user_login')
#         else:
#              messages.error(request,'Password doesnot matched')
#              return redirect('register')
#     else:
#         return render(request,'register.html')

# def register(request):
#     if request.method == 'POST':
#         print("POST request received")  # Add this line
        
#         email = request.POST['email']
        
#         first_name=request.POST['name']
#         password=request.POST['password']
#         username=request.POST['username']
#         cpassword=request.POST['cpassword']
#         if password==cpassword:
            
            
#             if User.objects.filter(email=email).exists():
                
#                 messages.error(request, 'Email already registered')
#                 return redirect('user_login')
#             else:
#                 user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
                
#                 user.save()
#                 messages.info(request, 'User created')
#                 email_subject='test subject for django'
#                 email_body='test message'
#                 email=EmailMessage(
#                     'email_subject',
#                     'email_body',
#                     'kazalzaswal@gmail.com',
#                     ['20dcs022@nith.ac.in']
#                 )
#                 email.send(fail_silently=False)
#                 return redirect('user_login')
#         else:
            
#             messages.error(request, 'Password does not match')
#             return redirect('register')
#     else:
        
#         return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        print("POST request received")  # Add this line
        
        email = request.POST['email']
        
        first_name=request.POST['name']
        password=request.POST['password']
        username=request.POST['username']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            
            # Remove this check for existing email here
            
            user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
            
            user.save()
            messages.info(request, 'User created')
            
            # email_subject = 'Test subject for django'
            email_subject = 'Welcome to candid'
            email_body = 'Test message'
            email = EmailMessage(
                email_subject,
                'Registration successful',
                'kazalzaswal@gmail.com',
                ['20dcs022@nith.ac.in','kaju7jaswal@gmail.com','20dcs013@nith.ac.in' ,'20bcs093@nith.ac.in ']
            )
            email.send(fail_silently=False)
            return redirect('user_login')
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
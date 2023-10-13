from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index1(request):
    return render(request, 'index1.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')
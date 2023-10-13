from django.shortcuts import render,get_object_or_404
from home.models import Category
from home.models import courses

# Create your views here.
def home(request):

    category=Category.objects.all().values()
    course=courses.objects.all().values()
    data={
          'course': course,
          'category':category,
          }

    return render(request,'home.html',data)

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def search(request):
    searches=request.GET['find']
    #print(searches)
    category=Category.objects.all()
    crs=courses.objects.filter(title__icontains=searches)
    res={'course':crs,
         'category':category}
    return render(request,'search.html',res)

def show_category(request,pkid):
    categ=Category.objects.get(id=pkid)
    category=Category.objects.all()
    course=courses.objects.filter(cate=categ)
    data={'course':course,
          'category':category
          }
    return render(request,'home.html',data)


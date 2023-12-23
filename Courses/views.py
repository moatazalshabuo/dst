from django.shortcuts import render,redirect
from .models import Courses
from .forms import *
# Create your views here.
def index(request):
    courses =  Courses.objects.all()
    return render(request,'courses/index.html',{'courses':courses})

def course(request,id):
    course = Courses.objects.get(pk=id)
    
    return render(request,'courses/course.html',{'course':course})

def regest(request,id):
    course = Courses.objects.get(pk=id)
    form = ClientsForms(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            cour = form.save(commit=False)
            cour.course = course
            cour.save()
            return redirect('course.success',id=cour.id)
    return render(request,'courses/register.html',{'course':course,'form':form})


def success(request,id):
    client = Clients.objects.get(pk=id)
    
    return render(request,'courses/success.html',{'client':client})
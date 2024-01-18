from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Departments,Doctors
from.forms import BookingForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

def index(request):
    return render(request,'index.html')


def about(request):
    departments = Departments.objects.all()
    doctors = Doctors.objects.all()
    return render(request, 'about.html', {'departments': departments, 'doctors': doctors})

@login_required(login_url='/')
def booking(request):
    if request.method =="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)


@login_required(login_url='/')
def doctors(request):
    dict_docs = {
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)




def contact(request):
   
    context = {
        'page_title': 'Contact', 
    }
    return render(request, 'contact.html', context)



@login_required(login_url='/')
def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)

def signup(request):
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('login')
    return render(request,'signup.html')

def login_view(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('signup')
    return render(request,'login.html')

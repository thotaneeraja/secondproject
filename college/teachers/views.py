from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import details
from.forms import detailsForm
from django.contrib.auth import authenticate, logout


def func(request):
    return HttpResponse("neeraja")
def cre(request):
    return HttpResponse("obulamma")
def index(request):
    data = details.objects.all()
    dict = {'studata': data}
    return render(request, 'index.html', dict)
def create(request):
    if request.method=='POST':

        form=detailsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
            form=detailsForm()
    return render(request,'create.html',{'form':form})
def edit(request,name):
     studata=details.objects.get(name=name)
     form=detailsForm(instance=studata)
     return render(request,'update.html',{'form':form,'name':name})
def delete(request,name):
    studata=details.objects.get(name=name)
    studata.delete()
    return redirect('/index/')

def update(request,name):
    studata=details.objects.get(name=name)
    form=detailsForm(request.POST,instance=studata)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    return render(request,'update.html',{'form':form,'name':name})

def login(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pwd=request.POST.get('password')
        user=authenticate(username=uname,password=pwd)

        if user:
            return redirect('/index/')
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return redirect('/login/')
def home(request):
    return render(request,'home.html')



# Create your views here.

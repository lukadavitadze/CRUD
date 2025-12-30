from django.shortcuts import render,redirect
from .models import person
import datetime
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    day = now.day
    month = now.month
    year = now.year
    if request.method == "POST":
        name = request.POST['name']
        lastname = request.POST['lastname']
        gmail = request.POST['gmail']
        date = f"{month}:{day}:{year}"

        add = person(name=name,lastname=lastname,gmail=gmail,time=date)
        add.save()
        return redirect('/show/')
    return render(request,'index.html')

def show(request):
    sh = person.objects.all()
    return render(request,'show.html',{'list':sh})

def delete(request,id):
    dele = person.objects.get(id=id)
    dele.delete()
    return redirect('/show/')

def edit(request,id):
    ed = person.objects.get(id=id)
    if request.method == "POST":
        n = request.POST['name']
        l = request.POST['lastname']
        g = request.POST['gmail']
        dic = person.objects.get(id=id)
        dic.name = n
        dic.lastname = l
        dic.gmail = g
        dic.save()
        return redirect('/show/')
         
    return render(request,'edit.html',{'list':ed})

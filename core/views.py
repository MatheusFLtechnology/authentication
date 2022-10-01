from pyexpat.errors import messages
from tkinter.messagebox import Message
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Restaurante
@login_required(login_url='/login/')
def list_all_restaurante(request):
    restaurante= Restaurante.objects.filter(active=True)
    return render(request, 'list.html', {'restaurante':restaurante})  
def list_user_restaurante(request):
    restaurante= Restaurante.objects.filter(active=True,user=request.user)
    return render(request, 'list.html',{'restaurante':restaurante})      

def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')

def restaurante_detail(request, id):
    restaurante = Restaurante.objects.get(active=True, id=id)
    print(restaurante.id)
    return render(request,'restaurante.html',{'restaurante':restaurante})


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username') 
        password = request.POST.get('password')   
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/') 
        else:
           messages.error(request,'usuário e senha invalido. favor tentar novamente')
    return redirect('/login/')           



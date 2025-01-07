from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

def Logear_aut(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usr=form.cleaned_data.get("username")
            pass_usr=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usr, password=pass_usr)
            if usuario is not None:
               login(request, usuario) 
               return redirect("Transaccion")
        else:
            msg="Usuario o password son incorrecto"
            form=AuthenticationForm()
            return render(request, "LoginApp/Login.html/", {"form":form,"msg":msg})
    
    form=AuthenticationForm()
    return render(request, "LoginApp/Login.html/", {"form":form})

class VRegister_aut(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request, "LoginApp/Register.html/", {"form":form})
    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect("Transaccion")
        else:
            for msj in form.error_messages:
                messages.error(request, form.error_messages[msj])
            return render(request, "LoginApp/Register.html/", {"form":form})   

class VRegister(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request, "LoginApp/Register.html/", {"form":form})
    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect("Home")
        else:
            for msj in form.error_messages:
                messages.error(request, form.error_messages[msj])
            return render(request, "LoginApp/Register.html/", {"form":form})   
        
def cerrar_login(request):
    logout(request)  
    return redirect("Home")

def Logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            
            nombre_usr=form.cleaned_data.get("username")
            pass_usr=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usr, password=pass_usr)
            if usuario is not None:
               
               login(request, usuario) 
               return redirect("Home")
        else:
            msg="Usuario o password son incorrecto"
            form=AuthenticationForm()
            return render(request, "LoginApp/Login.html/", {"form":form,"msg":msg})
    form=AuthenticationForm()
    return render(request, "LoginApp/Login.html/", {"form":form})
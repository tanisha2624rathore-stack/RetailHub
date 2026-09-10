from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def restration(request):
    return render(request,"restration_log.html")

def sign_up(request):
    if request.method=="POST":
        username=request.POST.get("user_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")

        if User.objects.filter(username=username).first():
            print("user already exits")
            return render(
                 request, "restration_log.html", 
                {"error": "Username already exists."}
            )
        if password != confirm_password:
            print("password not match")
            return render(
                         request, "restration_log.html", 
                        {"error": "password do not match."}
                    )        

        user=User.objects.create_user(
            username=username,
            password=password,
            email=email

        )
        print("user",user)
        return redirect("bussiness_set")
    return redirect("restration")  


def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")

        user=authenticate(email=email,password=password)
        print("error")
        if user:
            login(request,user)
        return redirect("bussiness_set")   
    return redirect("restration")   



def bussiness_set(request):
    return render(request,"business_restration.html")







# Create your views here.

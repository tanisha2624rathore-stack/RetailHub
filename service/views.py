from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import requests
import json 
from django.http import JsonResponse
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
                {"message": "Username already exists.",
                  "is_sign_up":True
                                          
                })
            
        if password != confirm_password:
            print("password not match")
            return render(
                         request, "restration_log.html", 
                        {"message": "password do not match.",
                         "is_sign_up":True
                         
                    })        

        user=User.objects.create_user(
            username=username,
            password=password,
            email=email

        )
        print("user",user)
        return redirect("bussiness_set")
    return redirect("restration")  


def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")      
        user=authenticate(request,username=username,password=password)    
        try:
            if user:
                login(request,user) 
                return redirect("bussiness_set")   
            else:
                print("wrong data")
                return render(request,"restration_log.html",
                            {"login_message":"invalid password, email",
                                "is_login":True

                })
        except Exception as e:
            print("error",e)
            return render(request,"restration_log.html",
                            {"login_message":"invalid password, email",
                                "is_login":True
                            })
    return redirect("restration")   



def bussiness_set(request):
    return render(request,"business_restration.html")

def purchase(request,id=None):
    data=[]
    if request.method=="GET":
        if id is not None:
            response=requests.get(f"http://127.0.0.1:8000/api/edit_purchase/{id}/",headers={'Content-Type': 'application/json'})
            rep=response.json()
            data=rep.get("result")
            return render(request,"purchase.html",{"data":data[0]})
        return render(request,"purchase.html",{"data":None})   

    if request.method=="POST":
        company_name=request.POST.get("company_name")
        product_name=request.POST.get("product_name")
        qty=request.POST.get("qty")
        price=request.POST.get("price")
        total_price=request.POST.get("total_price")
        data={
            "company_name":company_name,
            "product_name":product_name,
            "qty":qty,
            "price":price,
            "total_price":total_price
        }
        if id is None:
            json_data= json.dumps(data)
            response=requests.post("http://127.0.0.1:8000/api/add_purchase/",data=json_data,headers={'Content-Type': 'application/json'})
            print(response)
            return redirect("purchase_list")
        else:
            json_data= json.dumps(data)
            response=requests.post(f"http://127.0.0.1:8000/api/edit_purchase/{id}/",data=json_data,headers={'Content-Type': 'application/json'})
            print(response)
            return redirect("purchase_list")

    return render(request,"purchase.html")







def purchase_list(request):
    return render(request,"purchase_list.html")

def delete_purchase(request,id):
     response=requests.get(f"http://127.0.0.1:8000/api/delete_purchase_api/{id}/",headers={'Content-Type': 'application/json'})
     print(response)
     return render(request,"purchase_list.html")

def filter_purchase_data(request):
    if request.method=="GET":
        search_value=request.GET.get("search_input")
        print("s =====",search_value)
        data={
            "search_value":search_value
        }
        json_data=json.dumps(data)
        response=requests.get("http://127.0.0.1:8000/api/filter_purchase_api/",data=json_data,headers={'Content-Type': 'application/json'})
        data=response.json()
        print("res==",data)
        return JsonResponse(data)  
    return JsonResponse({"error": "Invalid request"}, status=400)  




# Create your views here.

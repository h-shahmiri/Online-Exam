from django.shortcuts import render, redirect
from users.models   import Profile
from django.http      import HttpResponse , JsonResponse
import json  ;  
from django.views     import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from users.forms       import LoginForm , RegisterForm
from django.contrib.auth  import authenticate , login , get_user_model
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.

# ========================= Register ============================================================

def Regstform(request):
    reg_form = RegisterForm(request.POST or None)

    if reg_form.is_valid():

        context = {
            "regst_form"  : reg_form,
            "regsubmit"   : "Registraion Success"
        }

        users = User.objects.all()

        firstname = reg_form.cleaned_data.get("firstname")
        lastname = reg_form.cleaned_data.get("lastname")
        username = reg_form.cleaned_data.get("username")
        for x in users:
            if x.username == username:
                return redirect("/users/register")

        email    = reg_form.cleaned_data.get("email")
        for x in users:
            if x.email == email:
                return redirect("/users/register")

        password = reg_form.cleaned_data.get("password1")
        password_hash = make_password(password=password)
        new_user = User(username=username , email=email , password=password_hash, first_name=firstname , last_name=lastname)
        new_user.save()

    else:
        context = {
            "regst_form"  : reg_form ,
            "regerror"    : "Error Please Check Details"
        }
        print("Error Registration")

    return render(request , "Register.html" , context)

    
# ========================= LOGIN ============================================================
@csrf_exempt
def Loginform(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "log_form" : login_form,
    }

    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user     = authenticate(username=username , password=password)

        users = User.objects.filter(username=username)

        for x in users:
            if check_password(password, x.password):
                username = x.username
                request.user.is_authenticated
                login(request ,user)
                return redirect("/")
            else:
                context = {
                    "log_form" : login_form,
                    "Error"    : "Error Username or Password is Wrong"
                }

    return render(request , "Login.html" , context)

#===============================================================================

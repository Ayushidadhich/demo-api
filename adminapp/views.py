from .models import *

from django.contrib.auth.hashers import make_password
import datetime


from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import auth ,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def homepage(request):
    template_name = 'index.html'
    # admin = User.objects.get(is_superuser = True)
    # u = User.objects.filter(is_superuser = False).count()
    # print(u,'uuuuuuuuuuuuuuuuuuuuuuuuuu'){'admin':admin , 'u':u}
    return render(request, template_name)


def adminlogin(request):
    template_name = 'admin-login.html'
    if request.method=='POST':
        email=request.POST.get('email')
        print(email,'yyyyyyyyyyyyy')
        password=request.POST.get('password')
        print(password,'ppppppppppp')
        try:
            admin = auth.authenticate(email=email,  password=password)
            print(admin, 'uuuuuuuuuuuuuuuuuuuuuuuu')
        except:
            admin: None
            print('ooooooooooooooooooooooooooooooooo')
        try:
            if admin.is_superuser == True:
                auth.login(request, admin)
                
                messages.success(request, "You have Successfully Login.")
                return redirect('homepage')
           # else:
               # messages.error(request, "Invalid username or password ")
               # return redirect('admin_login')
        except:
            messages.error(request, "Invalid username or password ")
            return redirect('admin_login')

    return render(request, template_name)

# Create your views here.

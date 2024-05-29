from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .form import RegisterCustomerForm


def register_cust(request):
    if request.method=='POST':
        form= RegisterCustomerForm(request.POST)
        if form.is_valid():
            var= form.save(commit= False)
            var.is_customer=True
            var.save()
            messages.info(request,'Your account has been successfully registered. Please login to Continue')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong !!!')
            return redirect('register_cust')
        
    else:
        form= RegisterCustomerForm()
        context = {'form':form}
        return render(request,'users/register_cust.html', context)
    

def login_user(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username= username, password= password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, 'Login successful. Please enjoy your session')
            return redirect('dashboard')
        else:
            messages.warning(request,'Something went wrong! Please enter valid input')
            return redirect('login')
    
    else :
        return render(request,'users/login.html')
    


def logout_user(request):
    logout(request)
    messages.info(request,'Your session has ended. Please log in to continue')
    return redirect('login')


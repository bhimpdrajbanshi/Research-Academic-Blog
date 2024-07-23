from django.shortcuts import render 
from django.contrib.auth import authenticate, login,logout

# Create your views here. 
def login_view(request):
	return render(request, "login.html") 

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request,"Login successfully")
                return redirect('/dashboard')  # Redirect to a different page, e.g., home page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please enter both username and password.")
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')
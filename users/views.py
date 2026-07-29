from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from .forms import SignUpForm

def home(request):
    return render(request, "welcome.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            print("USER CREATED:",user.username)
            return redirect("home")
    else:
        print(form.errors)

    return render(request, "signup.html", {
        "form": form
    })
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        else:
            print(form.errors)   # <-- Add this line

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("home")




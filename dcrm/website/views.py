from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.http import Http404
from .models import Customer


# Create your views here.
def home(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "User Logged In!")
            return redirect("home")
        else:
            raise Http404("User not found!")
            return redirect("home")
    else:
        return render(request, "home.html", {"customers": customers})


def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("home")


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")  # use password1 here
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f"Successfully registered {username}")
            print(f"Successfully registered {username}")
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def customer_records(request, id):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=id)
        print("🚀 ~ customer:", customer)
        return render(request, "customer.html", {"customer": customer})

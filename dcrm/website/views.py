from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, AddRecordForm
from .models import Customer


from django.shortcuts import render
from .models import Customer  # Assuming Customer model is imported from models.py


# Define your view function
def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        customers = Customer.objects.all()
        loggedInUser = request.user
        return render(
            request, "home.html", {"customers": customers, "loggedInUser": loggedInUser}
        )


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "User Logged In!")
            return redirect("home")
    else:
        return render(request, "login.html")


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


def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("home")


def customer_records(request, id):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=id)
        print("🚀 ~ customer:", customer)
        return render(request, "customer.html", {"customer": customer})


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New Customer Added")

        return render(request, "add_record.html", {"form": form})
    else:
        messages.success(request, "You must be logged in")
        return redirect("home")

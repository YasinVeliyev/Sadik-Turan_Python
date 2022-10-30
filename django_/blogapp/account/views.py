from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {"error": "İstifadəçi adı və ya Şifrə yanlışdır"})
    return render(request, "account/login.html")


def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                return render(request, "account/register.html", {"error": "Email və ya İstifadəçi adı mövcuddur", "username": username, "lastname": lastname, "email": email, "firstname": firstname})
            user = User.objects.create_user(
                username=username, email=email, first_name=firstname, last_name=lastname, password=password)
            user.save()
            return redirect("login")

        else:
            return render(request, "account/register.html", {"error": "Şifrələr uyğun gəlmir", "username": username, "lastname": lastname, "email": email, "firstname": firstname})
    return render(request, "account/register.html")


def logout_request(request):
    logout(request)
    return redirect("home")

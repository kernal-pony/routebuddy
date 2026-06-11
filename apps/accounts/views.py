from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render

from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

from .forms import UserRegistrationForm
from .forms import UserLoginForm

def register(request):

    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Account created successfully."
            )

            return redirect("accounts:login")

    else:

        form = UserRegistrationForm()

    context = {
        "form": form
    }

    return render(request, "accounts/register.html", context)

def user_login(request):

    if request.method == "POST":

        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request,user)

            messages.success(
                request,
                "Logged in successfully."
            )

            return redirect("routes:route_list")

    else:

        form = UserLoginForm()

    return render(request, "accounts/login.html",
        {
            "form": form
        }
    )

def user_logout(request):

    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect(
        "accounts:login"
    )
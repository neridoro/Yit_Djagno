from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth.models import User
#register view.
#make sure email is not taken by other user.
#renders the register html.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.username=obj.email
            if User.objects.filter(email=obj.email).exists():
                messages.error(response,"email alredy taken.")
            else:
                form.save()
                messages.info(response,"You have registered! please log in.")
                return  redirect("/login/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})
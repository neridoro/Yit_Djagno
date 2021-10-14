from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#rendering homepage
#allow only logged in users
@login_required
def homepage(request):
    return render(request, "homepage/homepage.html",{"first_name":request.user.first_name,"last_name":request.user.last_name})
#logging out function
#allow only logged in users 
@login_required
def logout_view(request):
    logout(request)
    return redirect("/login")
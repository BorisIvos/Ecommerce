from django.shortcuts import render,redirect

def singup(request):
    return render(request, "authentication/singup.html")

def handlelogin(request):
    return render(request, "authentication/login.html")

def handlelogout(request):
    return redirect('/authcart/login')
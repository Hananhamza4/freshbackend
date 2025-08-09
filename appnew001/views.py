from django.shortcuts import render
from django.http import HttpResponse

def hanan(request):
    return HttpResponse("hello world ")
def newfunc(request):
    return HttpResponse("new page !!!")
def newfunc01(request):
    return render(request,"index.html")
def loginfun(request):
    return render(request,"login.html")
def indexfun(request):
    return render(request,"index.html")
def error(request):
    return render(request,"404.html")
def about(request):
    return render(request,"about.html")
def cart(request):
    return render(request,"cart.html")
def checkout(request):
    return render(request,"checkout.html")
def contact(request):
    return render(request,"contact.html")
def news(request):
    return render(request,"news.html")
def shop(request):
    return render(request,"shop.html")
def signup(request):
    return render(request,"signup.html")
def singlen(request):
    return render(request,"single-news.html")
def singlep(request):
    return render(request,"single-product.html")



# Create your views here.

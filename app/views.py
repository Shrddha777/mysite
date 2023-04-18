from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def homePage(request):
    return render(request,"index.html")

def aboutUs(request):
    return HttpResponse("<h1>Welcome to Lagran Family</h1>")







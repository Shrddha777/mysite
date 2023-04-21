from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def homepage(request):
    return render(request,"index.html")

def about(request):
    return render(request,'app/static.html')

def contact(request):
    return render(request,'app/static.html/css')






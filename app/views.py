from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def homePage(request):
    data={
        'title':'Home Page',
        'bdata':'Welcome to mysite',
        'clist':['php','c','c++','Django'],
        'student_details':[
            {'Name':'Shrddha','Phone':8855949556},
            {'Name':'Nishu','Phone':7588425404}
        ]
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("<h1>Welcome to Lagran Family</h1>")







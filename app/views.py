from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index1(request):
    return render(request,"hellos.html")
# Create your views here.

def index2(request):
    return HttpResponse("<h1>welcome to india</h1>")

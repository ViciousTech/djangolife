from django.shortcuts import render
from quora.form import *
def home(request):
    return render(request,"home.html",{'form':login})
